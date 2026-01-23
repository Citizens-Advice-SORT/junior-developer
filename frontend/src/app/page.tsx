import Image from "next/image";
import Content from "@/components/Content";

export default async function Home() {
  // TODO: Fetch the data from /api/data

  return (
    <div className="font-sans grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20">
      <main className="flex flex-col gap-[32px] row-start-2 items-center sm:items-start">
        <div className="flex flex-col justify-center items-center w-full">
          <Image
            src="/logo.png"
            alt="Citizens Advice SORT"
            width={150}
            height={150}
            priority
          />
          <h1 className="text-2xl font-bold mt-4">
            Citizens Advice SORT
          </h1>
          <h2 className="text-lg font-medium">
            Junior Developer Practical
          </h2>
        </div>
        <Content /> {/* Each piece of content in the list should have its own content component */}
      </main>
    </div>
  );
}
