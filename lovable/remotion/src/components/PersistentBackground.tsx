import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate } from "remotion";

// Slow-drifting mint gradient blob + hairline rules + frame counter.
// Persists across the whole video to tie scenes together.
export const PersistentBackground: React.FC = () => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();

  // Background fades from cream-white to mint-white very slowly
  const bgMix = interpolate(frame, [0, 120], [0, 1], { extrapolateRight: "clamp" });
  const bg = `rgb(${244 + (244 - 244) * bgMix}, ${248 + (251 - 248) * bgMix}, ${244 + (249 - 244) * bgMix})`;

  // Drifting blob position (very slow sinusoidal)
  const t = frame / 60;
  const blobX = 60 + Math.sin(t * 0.4) * 6;
  const blobY = 45 + Math.cos(t * 0.3) * 5;
  const blobScale = 1 + Math.sin(t * 0.5) * 0.08;

  // Hairlines: draw in at start, stay
  const hairlineProgress = interpolate(frame, [10, 70], [0, 1], { extrapolateRight: "clamp" });

  // Frame counter
  const totalSeconds = Math.floor(durationInFrames / 30);
  const currentSecond = Math.min(Math.floor(frame / 30) + 1, totalSeconds);
  const counterText = `${String(currentSecond).padStart(2, "0")} — ${String(totalSeconds).padStart(2, "0")}`;

  return (
    <AbsoluteFill style={{ background: bg, fontFamily: "Inter, sans-serif" }}>
      {/* Soft mint gradient blob */}
      <div
        style={{
          position: "absolute",
          left: `${blobX}%`,
          top: `${blobY}%`,
          width: 1400,
          height: 1400,
          transform: `translate(-50%, -50%) scale(${blobScale})`,
          background:
            "radial-gradient(circle at center, rgba(20,184,166,0.18) 0%, rgba(20,184,166,0.08) 30%, rgba(20,184,166,0) 65%)",
          filter: "blur(40px)",
          pointerEvents: "none",
        }}
      />
      {/* Secondary warm blob */}
      <div
        style={{
          position: "absolute",
          left: `${20 - Math.sin(t * 0.3) * 4}%`,
          top: `${80 + Math.cos(t * 0.25) * 3}%`,
          width: 900,
          height: 900,
          transform: "translate(-50%, -50%)",
          background:
            "radial-gradient(circle at center, rgba(239,233,223,0.55) 0%, rgba(239,233,223,0) 60%)",
          filter: "blur(30px)",
          pointerEvents: "none",
        }}
      />

      {/* Top hairline */}
      <div
        style={{
          position: "absolute",
          top: 80,
          left: 80,
          right: 80,
          height: 1,
          background: "#0B2A2A",
          opacity: 0.35,
          transform: `scaleX(${hairlineProgress})`,
          transformOrigin: "left center",
        }}
      />
      {/* Bottom hairline */}
      <div
        style={{
          position: "absolute",
          bottom: 80,
          left: 80,
          right: 80,
          height: 1,
          background: "#0B2A2A",
          opacity: 0.35,
          transform: `scaleX(${hairlineProgress})`,
          transformOrigin: "right center",
        }}
      />

      {/* Eyebrow top-left label */}
      <div
        style={{
          position: "absolute",
          top: 50,
          left: 80,
          fontSize: 13,
          letterSpacing: 4,
          color: "#0B2A2A",
          opacity: 0.65 * hairlineProgress,
          fontWeight: 500,
        }}
      >
        AXIOM — STUDY № 01
      </div>
      {/* Frame counter top-right */}
      <div
        style={{
          position: "absolute",
          top: 50,
          right: 80,
          fontSize: 13,
          letterSpacing: 4,
          color: "#0B2A2A",
          opacity: 0.65 * hairlineProgress,
          fontVariantNumeric: "tabular-nums",
          fontWeight: 500,
        }}
      >
        {counterText}
      </div>
      {/* Bottom-left footer label */}
      <div
        style={{
          position: "absolute",
          bottom: 50,
          left: 80,
          fontSize: 11,
          letterSpacing: 3,
          color: "#0B2A2A",
          opacity: 0.5 * hairlineProgress,
        }}
      >
        CLARITY · BY DESIGN
      </div>
      <div
        style={{
          position: "absolute",
          bottom: 50,
          right: 80,
          fontSize: 11,
          letterSpacing: 3,
          color: "#0B2A2A",
          opacity: 0.5 * hairlineProgress,
        }}
      >
        MMXXVI
      </div>
    </AbsoluteFill>
  );
};
