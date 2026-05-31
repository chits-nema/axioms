import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate, spring } from "remotion";

// Scene 3: Three large overlapping translucent teal circles settle off-center
export const Scene3: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const circles = [
    { dx: -120, dy: 0, color: "rgba(20,184,166,0.35)", delay: 0 },
    { dx: 80, dy: -60, color: "rgba(15,118,110,0.30)", delay: 8 },
    { dx: 40, dy: 90, color: "rgba(110,231,183,0.40)", delay: 16 },
  ];

  const inOpacity = interpolate(frame, [0, 25], [0, 1], { extrapolateRight: "clamp" });
  const outOpacity = interpolate(frame, [85, 105], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });

  return (
    <AbsoluteFill style={{ alignItems: "center", justifyContent: "center", opacity: inOpacity * outOpacity }}>
      <div style={{ position: "relative", width: 800, height: 600, marginLeft: 160 }}>
        {circles.map((c, i) => {
          const p = spring({
            frame: frame - c.delay,
            fps,
            config: { damping: 26, stiffness: 90, mass: 1 },
          });
          const size = 360 * p;
          const x = 400 + c.dx - size / 2;
          const y = 300 + c.dy - size / 2;
          return (
            <div
              key={i}
              style={{
                position: "absolute",
                left: x,
                top: y,
                width: size,
                height: size,
                borderRadius: "50%",
                background: c.color,
                mixBlendMode: "multiply",
              }}
            />
          );
        })}
      </div>
      {/* Small caps label, far left to anchor composition */}
      <div
        style={{
          position: "absolute",
          left: 200,
          top: "50%",
          transform: "translateY(-50%)",
          fontFamily: "Inter, sans-serif",
          fontSize: 12,
          letterSpacing: 5,
          color: "#0B2A2A",
          opacity: interpolate(frame, [30, 60], [0, 0.7], { extrapolateRight: "clamp" }),
          writingMode: "vertical-rl",
          fontWeight: 500,
        }}
      >
        FIG. 03 · CONVERGENCE
      </div>
    </AbsoluteFill>
  );
};
