import type { Metadata } from "next";
import { Open_Sans } from "next/font/google";

import "./globals.css";

const openSans = Open_Sans({
  variable: "--font-open-sans",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Junior Developer | CASORT",
  description: "Citizens Advice SORT Junior Developer practical",
};

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html lang="en">
      <body
        className={`${openSans.variable} min-h-dvh bg-background font-sans text-foreground antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
