import fs from "fs";
import path from "path";

const CHAPTERS_DIR = path.join(process.cwd(), "manuscript", "chapters");

export type ChapterMeta = {
  slug: string;
  order: number;
  title: string;
  subtitle: string;
  filename: string;
};

function parseFilename(filename: string): { order: number; slug: string } {
  const match = filename.match(/^(\d+)-(.+)\.md$/);
  if (!match) {
    throw new Error(`Unexpected chapter filename: ${filename}`);
  }
  return { order: Number(match[1]), slug: match[2] };
}

function extractTitleAndSubtitle(markdown: string): {
  title: string;
  subtitle: string;
} {
  const lines = markdown.split("\n").map((l) => l.trim());
  const titleLine = lines.find((l) => l.startsWith("# "));
  const title = titleLine ? titleLine.slice(2).trim() : "Untitled";
  const subtitleLine = lines.find(
    (l) => l.startsWith("*") && l.endsWith("*") && !l.startsWith("**"),
  );
  const subtitle = subtitleLine
    ? subtitleLine.replace(/^\*/, "").replace(/\*$/, "")
    : "";
  return { title, subtitle };
}

export function listChapters(): ChapterMeta[] {
  if (!fs.existsSync(CHAPTERS_DIR)) return [];
  const files = fs.readdirSync(CHAPTERS_DIR).filter((f) => f.endsWith(".md"));
  return files
    .map((filename) => {
      const { order, slug } = parseFilename(filename);
      const raw = fs.readFileSync(path.join(CHAPTERS_DIR, filename), "utf8");
      const { title, subtitle } = extractTitleAndSubtitle(raw);
      return { slug, order, title, subtitle, filename };
    })
    .sort((a, b) => a.order - b.order);
}

export function getChapterBySlug(
  slug: string,
): (ChapterMeta & { markdown: string }) | null {
  const chapter = listChapters().find((c) => c.slug === slug);
  if (!chapter) return null;
  const markdown = fs.readFileSync(
    path.join(CHAPTERS_DIR, chapter.filename),
    "utf8",
  );
  return { ...chapter, markdown };
}
