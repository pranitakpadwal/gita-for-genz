import Link from "next/link";
import { notFound } from "next/navigation";
import { marked } from "marked";
import type { Metadata } from "next";
import { getChapterBySlug, listChapters } from "@/lib/chapters";

type RouteParams = { slug: string };

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

  const html = marked.parse(chapter.markdown, { async: false }) as string;

  return (
    <main className="mx-auto max-w-2xl px-6 py-16 sm:py-24">
      <Link
        href="/"
        className="text-sm text-muted hover:text-accent transition-colors"
      >
        &larr; Table of contents
      </Link>

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
