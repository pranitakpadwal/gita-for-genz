import type { Metadata } from "next";
import { Lora, Fraunces } from "next/font/google";
import "./globals.css";

const lora = Lora({
  variable: "--font-lora",
  subsets: ["latin"],
});

const fraunces = Fraunces({
  variable: "--font-fraunces",
  subsets: ["latin"],
  weight: ["500", "600", "700"],
});

export const metadata: Metadata = {
  title: "Gita for Gen Z — Preview",
  description:
    "A chapter-by-chapter preview of the Bhagavad Gita retold for Gen Z: real scenes, real shlokas, one takeaway per chapter.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={`${lora.variable} ${fraunces.variable}`}>
      <body className="min-h-screen antialiased">{children}</body>
    </html>
  );
}
