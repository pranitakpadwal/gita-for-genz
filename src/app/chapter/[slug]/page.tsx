import fs from "fs";
import path from "path";
import Link from "next/link";
import { notFound } from "next/navigation";
import { Marked } from "marked";
import type { Metadata } from "next";
import { getChapterBySlug, listChapters } from "@/lib/chapters";

type RouteParams = { slug: string };

const SECTION_ICONS: Record<string, string> = {
  Scene: "/icons/scene.svg",
  Shloka: "/icons/shloka.svg",
  "Why It Lands": "/icons/why-it-lands.svg",
  Takeaway: "/icons/takeaway.svg",
};

function renderChapterHtml(markdown: string): string {
  const marked = new Marked({
    renderer: {
      heading(text: string, level: number, raw: string) {
        const icon = level === 2 ? SECTION_ICONS[raw] : undefined;
        const iconImg = icon
          ? `<img src="${icon}" alt="" class="section-icon" width="28" height="28" />`
          : "";
        return `<h${level}>${iconImg}<span>${text}</span></h${level}>`;
      },
    },
  });
  return marked.parse(markdown, { async: false }) as string;
}

export function generateStaticParams() {
  return listChapters().map((chapter) => ({ slug: chapter.slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<RouteParams>;
}): Promise<Metadata> {
  const { slug } = await params;
  const chapter = getChapterBySlug(slug);
  if (!chapter) return { title: "Chapter not found" };
  return { title: `${chapter.title} — Gita for Gen Z` };
}

export default async function ChapterPage({
  params,
}: {
  params: Promise<RouteParams>;
}) {
  const { slug } = await params;
  const chapter = getChapterBySlug(slug);
  if (!chapter) notFound();

  const chapters = listChapters();
  const index = chapters.findIndex((c) => c.slug === slug);
  const prev = index > 0 ? chapters[index - 1] : null;
  const next = index < chapters.length - 1 ? chapters[index + 1] : null;

  const html = renderChapterHtml(chapter.markdown);
  const illustrationPath = path.join(
    process.cwd(),
    "public/illustrations",
    `${slug}.svg`,
  );
  const hasIllustration = fs.existsSync(illustrationPath);

  return (
    <main className="mx-auto max-w-2xl px-6 py-16 sm:py-24">
      <Link
        href="/"
        className="text-sm text-muted hover:text-accent transition-colors"
      >
        &larr; Table of contents
      </Link>

      {hasIllustration && (
        // eslint-disable-next-line @next/next/no-img-element
        <img
          src={`/illustrations/${slug}.svg`}
          alt=""
          className="mt-8 w-full rounded-sm border border-line"
        />
      )}

      <article
        className="prose-chapter mt-8"
        dangerouslySetInnerHTML={{ __html: html }}
      />

      <nav className="mt-16 pt-8 border-t border-line flex items-center justify-between text-sm">
        {prev ? (
          <Link
            href={`/chapter/${prev.slug}`}
            className="text-muted hover:text-accent transition-colors"
          >
            &larr; {prev.title}
          </Link>
        ) : (
          <span />
        )}
        {next ? (
          <Link
            href={`/chapter/${next.slug}`}
            className="text-muted hover:text-accent transition-colors text-right"
          >
            {next.title} &rarr;
          </Link>
        ) : (
          <span />
        )}
      </nav>
    </main>
  );
}
