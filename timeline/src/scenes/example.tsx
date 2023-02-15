import { makeScene2D } from '@motion-canvas/2d/lib/scenes';
import { Text, Node, Rect } from '@motion-canvas/2d/lib/components';
import { createRef } from '@motion-canvas/core/lib/utils';
import { all } from '@motion-canvas/core/lib/flow';
import books from '../../public/package-lock.json'
import { createSignal } from '@motion-canvas/core/lib/signals';
export default makeScene2D(function* (view) {
  const myRect = createRef<Rect>();
  const myWidth = createSignal(0)
  const myHeight = createSignal(0)
  const myYear = createSignal()
  const myText = createRef<Text>()
  const myOpacity = createSignal(0)
  view.add(
    <>
      <Rect
        ref={myRect}
        x={-400}
        width={() => myWidth()}
        height={() => myHeight()}
        fill="#e13238">
        <Text
          text={() => 'Year = ' + Math.round(myYear())}
          fill="#FFFF"
          opacity={() => parseFloat(myOpacity())}
        ></Text>
      </Rect>
    </>
  );

  yield* all(
    myWidth(0, 0).to(2000, 4),
    myRect().position.x(-500, 0).to(0, 1),
    myRect().position.y(0, 0).to(300, 2),
    myRect().fill('#e6a700', 1).to('#e13238', 1),
    myHeight(100, 4).to(400, 4),
    myRect().position.y(300, 4).to(0, 4),
    myYear(-350, 4).to(2023, 4),
    myOpacity(0, 4).to(1, 4)
  );
});