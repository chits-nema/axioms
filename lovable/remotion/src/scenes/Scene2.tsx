import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate, spring } from "remotion";

// Scene 2: Constellation of small filled teal dots drift outward from center
export const Scene2: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Generate stable dot constellation
  const dots = Array.from({ length: 36 }).map((_, i) => {
    // Two concentric rings + scattered
    const ring = i < 12 ? 0 : i < 24 ? 1 : 2;
    const angleOffset = ring * 0.3;
    const idx = ring === 0 ? i : ring === 1 ? i - 12 : i - 24;
    const count = ring === 0 ? 12 : ring === 1 ? 12 : 12;
    const angle = (idx / count) * Math.PI * 2 + angleOffset;
    const targetRadius = 90 + ring * 110;
    return { angle, targetRadius, delay: i * 0.8 };
  });

  const outOpacity = interpolate(frame, [85, 105], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const inOpacity = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: "clamp" });

  return (
    <AbsoluteFill style={{ alignItems: "center", justifyContent: "center", opacity: outOpacity * inOpacity }}>
      <div style={{ position: "relative", width: 700, height: 700 }}>
        {dots.map((d, i) => {
          const progress = spring({
            frame: frame - d.delay,
            fps,
            config: { damping: 28, stiffness: 70, mass: 1 },
          });
          const r = progress * d.targetRadius;
          const x = 350 + Math.cos(d.angle) * r;
          const y = 350 + Math.sin(d.angle) * r;
          const size = 6 + (i % 3) * 2;
          const opacity = progress * (0.5 + (i % 4) * 0.12);
          return (
            <div
              key={i}
              style={{
                position: "absolute",
                left: x - size / 2,
                top: y - size / 2,
                width: size,
                height: size,
                borderRadius: "50%",
                background: i % 5 === 0 ? "#0F766E" : "#14B8A6",
                opacity,
              }}
            />
          );
        })}
        {/* Faint center anchor */}
        <div
          style={{
            position: "absolute",
            left: 346,
            top: 346,
            width: 8,
            height: 8,
            borderRadius: "50%",
            background: "#0B2A2A",
            opacity: 0.7,
          }}
        />
      </div>
    </AbsoluteFill>
  );
};
