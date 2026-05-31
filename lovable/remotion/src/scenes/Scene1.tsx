import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate, spring } from "remotion";

// Scene 1: A single thin teal circle outline draws itself at center, label fades in
export const Scene1: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const drawProgress = interpolate(frame, [10, 80], [0, 1], {
    extrapolateRight: "clamp",
  });
  const labelOpacity = spring({ frame: frame - 50, fps, config: { damping: 200, mass: 1 } });
  const labelRise = interpolate(labelOpacity, [0, 1], [12, 0]);

  // Fade out at scene end
  const outOpacity = interpolate(frame, [85, 105], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });

  const radius = 180;
  const circumference = 2 * Math.PI * radius;

  return (
    <AbsoluteFill style={{ alignItems: "center", justifyContent: "center", opacity: outOpacity }}>
      <svg width={500} height={500} style={{ overflow: "visible" }}>
        <circle
          cx={250}
          cy={250}
          r={radius}
          fill="none"
          stroke="#0F766E"
          strokeWidth={1.2}
          strokeDasharray={circumference}
          strokeDashoffset={circumference * (1 - drawProgress)}
          transform="rotate(-90 250 250)"
        />
      </svg>
      <div
        style={{
          marginTop: 36,
          fontFamily: "Inter, sans-serif",
          fontSize: 14,
          letterSpacing: 8,
          color: "#0B2A2A",
          opacity: labelOpacity * 0.85,
          transform: `translateY(${labelRise}px)`,
          fontWeight: 500,
        }}
      >
        AXIOM
      </div>
    </AbsoluteFill>
  );
};
