
## Goal

Produce a ~15s, 1920x1080, 30fps MP4 hero video for Axiom's landing page. Pure **abstract art motion** — no product UI, no charts, no bars. Bright, airy, editorial. Slow and cinematic pacing. Soft mint/teal on near-white. Embedded as the autoplaying hero element on the landing page.

## Creative direction

- **Palette**: Background `#F4FBF9` (off-white mint). Ink `#0B2A2A`. Primary teal `#14B8A6`. Deep teal `#0F766E`. Warm cream accent `#EFE9DF`. Soft mint `#E6F4F1`.
- **Typography**: `Instrument Serif` (display), `Inter` (small caps labels). Both via `@remotion/google-fonts`.
- **Aesthetic**: Editorial minimalism. Generous whitespace. Off-center compositions. Thin hairlines. Tiny tracked-caps labels as visual accents only — no marketing copy.
- **Motion system**: One entrance — clip-path reveal + 12px rise, spring `{damping: 26, stiffness: 90}` (slow, smooth). Long fades (30–45f). Persistent slow drift on background. Soft fade-through transitions between scenes.

## Visual concept (abstract art only)

A meditative drift through geometric forms in soft teal — circles, hairlines, dots, and gradient blobs that breathe, expand, and reorganize. No product references, no UI mockups, no charts. Think Kinfolk-magazine-meets-Apple-product-film.

## Scene plan (~15s, 450 frames @ 30fps, slow pacing)

1. **Open (0–105f)** — Black-to-mint background eases in. A single thin teal circle outline draws itself slowly at the center. Tiny tracked label "AXIOM" fades in below.
2. **Bloom (105–210f)** — That circle multiplies into a slow-orbiting constellation of small filled teal dots that drift outward in formation. Soft mint gradient blob breathes in the background.
3. **Stack (210–315f)** — Dots dissolve into three large overlapping translucent teal circles that slowly settle into a stacked composition (Venn-like, off-center). Thin hairline rules slide in from edges.
4. **Word (315–405f)** — Circles fade to soft outlines. The serif word "Axiom" reveals via clip-path, large and off-center, with the tagline "Clarity, by design." in small caps underneath.
5. **Close (405–450f)** — Everything settles. Hairlines close in. Final still composition holds for the loop point.

Persistent layers across all scenes: slow-drifting mint gradient blob, faint top/bottom hairline rules, tiny frame counter in corner ("01 — 05") for editorial feel.

## Technical approach

- Scaffold a `remotion/` project per the video-creator skill (bun init, install remotion + transitions + google-fonts + compositor + renderer, fix musl/gnu compositor binary, symlink ffmpeg/ffprobe).
- Files: `src/index.ts`, `src/Root.tsx`, `src/MainVideo.tsx`, `src/scenes/Scene1…5.tsx`, `src/components/PersistentBackground.tsx`, `scripts/render-remotion.mjs`.
- All animation via `useCurrentFrame()` + `interpolate()` / `spring()`. No CSS animations, no `backdropFilter`.
- Render via the programmatic script (`chromeMode: "chrome-for-testing"`, `muted: true`, concurrency 1) to `/mnt/documents/axiom-hero.mp4`.
- Spot-check 3 key frames with `bunx remotion still` before the full render; iterate if any frame looks off.

## Landing page integration

- Copy the rendered MP4 to `public/axiom-hero.mp4`.
- Replace placeholder in `src/routes/index.tsx` with a real bright-themed Axiom landing page (light bg, mint/teal accents, Instrument Serif + Inter). Embed video as autoplaying, muted, looping, `playsInline` hero element.
- Update light tokens in `src/styles.css` to match palette.
- Update route `head()` with Axiom title/description.

## Deliverable

- `/mnt/documents/axiom-hero.mp4`
- Bright-themed Axiom landing page at `/` with the abstract video in the hero
