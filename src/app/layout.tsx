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
  title: "Krishna Texts Back — Preview",
  description:
    "18 Fights You're Already In — the Bhagavad Gita retold through real scenes, real shlokas, one takeaway per chapter.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={`${lora.variable} ${fraunces.variable}`}>
      <body className="min-h-screen antialiased">
        <div className="page-motifs" aria-hidden="true">
          {/* eslint-disable @next/next/no-img-element */}
          <img src="/motifs/peacock-feather.svg" className="motif motif-peacock" alt="" />
          <img src="/motifs/chakra.svg" className="motif motif-chakra" alt="" />
          <img src="/motifs/lotus.svg" className="motif motif-lotus" alt="" />
          <img src="/motifs/shankha.svg" className="motif motif-shankha" alt="" />
          <img src="/motifs/chariot-wheel.svg" className="motif motif-wheel" alt="" />
          {/* eslint-enable @next/next/no-img-element */}
        </div>
        {children}
      </body>
    </html>
  );
}
