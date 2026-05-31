import { AbsoluteFill, Sequence } from "remotion";
import { PersistentBackground } from "./components/PersistentBackground";
import { Scene1 } from "./scenes/Scene1";
import { Scene2 } from "./scenes/Scene2";
import { Scene3 } from "./scenes/Scene3";
import { Scene4 } from "./scenes/Scene4";
import { Scene5 } from "./scenes/Scene5";

// 450 frames total @ 30fps = 15s.
// Scenes overlap slightly via their internal fade-in/out to create soft cross-fades.
export const MainVideo: React.FC = () => {
  return (
    <AbsoluteFill>
      <PersistentBackground />
      <Sequence from={0} durationInFrames={105}>
        <Scene1 />
      </Sequence>
      <Sequence from={95} durationInFrames={115}>
        <Scene2 />
      </Sequence>
      <Sequence from={200} durationInFrames={115}>
        <Scene3 />
      </Sequence>
      <Sequence from={305} durationInFrames={100}>
        <Scene4 />
      </Sequence>
      <Sequence from={395} durationInFrames={55}>
        <Scene5 />
      </Sequence>
    </AbsoluteFill>
  );
};
