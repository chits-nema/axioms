import { AbsoluteFill, useCurrentFrame, interpolate } from "remotion";
import { loadFont as loadSerif } from "@remotion/google-fonts/InstrumentSerif";

const { fontFamily: serif } = loadSerif();

// Scene 5: Final still — small serif wordmark, centered, hairlines close in. Holds for loop.
export const Scene5: React.FC = () => {
  const frame = useCurrentFrame();

  const inOpacity = interpolate(frame, [0, 25], [0, 1], { extrapolateRight: "clamp" });
  // Hold most of scene, slight breath
  const breath = 1 + Math.sin(frame / 20) * 0.005;

  // Subtle final teal dot accent
  const dotP = interpolate(frame, [10, 45], [0, 1], { extrapolateRight: "clamp" });

  return (
    <AbsoluteFill style={{ alignItems: "center", justifyContent: "center", opacity: inOpacity }}>
      <div style={{ display: "flex", alignItems: "center", gap: 18, transform: `scale(${breath})` }}>
        <div
          style={{
            width: 10,
            height: 10,
            borderRadius: "50%",
            background: "#14B8A6",
            opacity: dotP,
          }}
        />
        <div
          style={{
            fontFamily: serif,
            fontSize: 92,
            color: "#0B2A2A",
            letterSpacing: -1,
            fontStyle: "italic",
          }}
        >
          Axiom
        </div>
      </div>
    </AbsoluteFill>
  );
};
