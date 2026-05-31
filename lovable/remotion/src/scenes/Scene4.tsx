import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate, spring } from "remotion";
import { loadFont as loadSerif } from "@remotion/google-fonts/InstrumentSerif";
import { loadFont as loadInter } from "@remotion/google-fonts/Inter";

const { fontFamily: serif } = loadSerif();
const { fontFamily: inter } = loadInter();

// Scene 4: Big serif "Axiom" reveals off-center via clip-path, tagline beneath
export const Scene4: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Reveal width (clip-path) for the serif word
  const revealP = spring({ frame: frame - 5, fps, config: { damping: 30, stiffness: 75 } });
  const clipRight = (1 - revealP) * 100;
  const wordRise = interpolate(revealP, [0, 1], [16, 0]);

  const taglineOpacity = spring({ frame: frame - 40, fps, config: { damping: 200 } });
  const taglineRise = interpolate(taglineOpacity, [0, 1], [10, 0]);

  // Soft outline circle ghost in background
  const ghostP = interpolate(frame, [0, 60], [0, 1], { extrapolateRight: "clamp" });

  const inOpacity = interpolate(frame, [0, 15], [0, 1], { extrapolateRight: "clamp" });
  const outOpacity = interpolate(frame, [78, 90], [1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });

  return (
    <AbsoluteFill style={{ opacity: inOpacity * outOpacity }}>
      {/* Ghost circle outline */}
      <svg
        width={600}
        height={600}
        style={{ position: "absolute", left: "55%", top: "50%", transform: "translate(-50%, -50%)" }}
      >
        <circle cx={300} cy={300} r={260} fill="none" stroke="#0F766E" strokeWidth={1} opacity={0.25 * ghostP} />
        <circle cx={300} cy={300} r={200} fill="none" stroke="#0F766E" strokeWidth={1} opacity={0.18 * ghostP} />
      </svg>

      {/* Off-center word block */}
      <div
        style={{
          position: "absolute",
          left: "12%",
          top: "44%",
          transform: `translateY(calc(-50% + ${wordRise}px))`,
        }}
      >
        <div
          style={{
            fontFamily: serif,
            fontSize: 260,
            lineHeight: 0.95,
            color: "#0B2A2A",
            letterSpacing: -4,
            clipPath: `inset(0 ${clipRight}% 0 0)`,
            fontStyle: "italic",
          }}
        >
          Axiom
        </div>
        <div
          style={{
            marginTop: 32,
            marginLeft: 6,
            fontFamily: inter,
            fontSize: 14,
            letterSpacing: 6,
            color: "#0B2A2A",
            opacity: taglineOpacity * 0.75,
            transform: `translateY(${taglineRise}px)`,
            fontWeight: 500,
          }}
        >
          CLARITY, BY DESIGN
        </div>
      </div>
    </AbsoluteFill>
  );
};
