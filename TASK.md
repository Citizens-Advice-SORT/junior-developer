# The task

This is the practical for the Junior Developer role at Citizens Advice SORT.

The app shows answers to advisers' questions, along with the sources each answer is based on. Your job is to finish it: link each answer to its sources, and hide the client's personal details in each question.

Follow [SETUP.md](SETUP.md) first to get the app running.

## What's already set up

- `GET /data` returns the four items in `backend/data/mock.json`.
- The redaction model loads when the backend starts. To use it in an endpoint, add `model: GLiNER2 = Depends(get_model)` (see `backend/app/dependencies.py`).
- The backend accepts requests from the frontend at http://localhost:3000, so you can call it from any component.
- `frontend/app/page.tsx` has a `ContentList` component for fetching the data, and `frontend/components/Content.tsx` is where each item goes.

You can change any of it, including the shape of the data in `backend/app/models.py`.

## The data

Each item looks like this (shortened):

```json
{
    "category": "consumer_goods_and_services",
    "question": "My client Sarah Jones had her mobile phone stolen last Friday. What should she do? ...",
    "sources": [
        {
            "id": "GOMgBJgBBLViOYD198L",
            "title": "What to do if your mobile phone is lost or stolen - Citizens Advice",
            "source": "https://citizensadvice.org.uk/consumer/phone-internet-downloads-or-tv/what-to-do-if-your-mobile-phone-is-lost-or-stolen"
        }
    ],
    "content": "If your client's mobile phone was stolen last Friday, they should take the following steps based on the information available <ref>GOMgBJgBBLViOYD198L</ref>: ..."
}
```

- `question` is what the adviser asked. It contains the client's name, email address and phone number.
- `content` is the answer. It cites sources with `<ref>id</ref>`, where `id` is a source's `id`. It also contains some HTML, such as `<b>`.
- `sources` lists the sources for the answer. Not all of them are cited.

## Backend

Do this work in the backend, so that `GET /data` returns the finished data.

### 1. Link the citations

1. Work out which sources each answer cites.
2. Replace each `<ref>id</ref>` with a link to that source.
3. Get the favicon for each source's website.

### 2. Redact the question

Replace the client's personal details in each `question` with placeholders, so the real details never leave the backend.

| Find (model label) | Replace with |
|---|---|
| `full_name`, `first_name`, `last_name` | `[NAME]` |
| `email` | `[EMAIL]` |
| `phone_number` | `[PHONE]` |

For example, "Call Alex Smith on 07700 900000 or email alex.smith@example.com." becomes "Call [NAME] on [PHONE] or email [EMAIL]."

1. Use the model to find the details. Pass `include_spans=True` so you get where each one starts and ends in the text.
2. Turn each one into a Presidio `RecognizerResult`, and use Presidio's `AnonymizerEngine` to replace them.

The model can find the same name more than once: "Alex Smith" as a full name, and "Alex" and "Smith" on their own. Each name should still become one `[NAME]`, not `[NAME] [NAME]`. Presidio's docs explain how it handles finds that overlap.

You can check your work at http://localhost:8000/docs by trying `GET /data`.

## Frontend

In `Content.tsx`, show each item with:

1. The redacted question.
2. The answer, with its citations as working links.
3. All of its sources, cited and not cited, each with its favicon.

Make it clean and easy to read.

## Useful links

- GLiNER2: https://github.com/fastino-ai/GLiNER2
- The redaction model: https://huggingface.co/fastino/GLiNER2-Guardrails-PII-Multi
- Presidio anonymizer: https://data-privacy-stack.github.io/presidio/anonymizer/

## Submission

Please respond to the invitation email with a link to your complete repository.

Please also add a short `NOTES.md` with the choices you made, and anything that didn't work.

> If you have any problems or are unsure about any of the steps please email technology@casort.org
