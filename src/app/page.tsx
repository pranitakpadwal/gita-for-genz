import Link from "next/link";
import { listChapters } from "@/lib/chapters";

export default function HomePage() {
  const chapters = listChapters();

  return (
    <main className="mx-auto max-w-2xl px-6 py-16 sm:py-24">
      <p className="text-sm uppercase tracking-[0.2em] text-muted mb-3">
        Work in progress · preview build
      </p>
      <h1 className="font-display text-4xl sm:text-5xl font-semibold mb-2">
        Krishna Texts Back
      </h1>
      <p className="font-display text-xl italic text-accent mb-6">
        18 Fights You&rsquo;re Already In
      </p>
      <p className="text-lg text-muted leading-relaxed mb-12">
        The Bhagavad Gita&rsquo;s 18 chapters, retold through the situations
        we actually live in. Each fight: a real scene, the actual shloka,
        one takeaway.
      </p>

      <ol className="space-y-1">
        {chapters.map((chapter) => (
          <li key={chapter.slug}>
            <Link
              href={`/chapter/${chapter.slug}`}
              className="group flex items-baseline gap-4 py-3 border-b border-line hover:bg-accent-soft/60 -mx-3 px-3 rounded transition-colors"
            >
              <span className="font-display text-sm text-muted w-6 shrink-0">
                {String(chapter.order).padStart(2, "0")}
              </span>
              <span className="flex-1">
                <span className="block font-medium group-hover:text-accent transition-colors">
                  {chapter.title}
                </span>
                {chapter.subtitle && (
                  <span className="block text-sm text-muted italic">
                    {chapter.subtitle}
                  </span>
                )}
              </span>
            </Link>
          </li>
        ))}
        {chapters.length === 0 && (
          <li className="text-muted italic py-6">
            No fights drafted yet — check back soon.
          </li>
        )}
      </ol>

      {chapters.length > 0 && chapters.length < 18 && (
        <p className="mt-12 text-sm text-muted">
          {chapters.length} of 18 fights drafted so far. This is a preview
          build, not the final manuscript — content, order, and design are
          all still in progress.
        </p>
      )}
    </main>
  );
}
