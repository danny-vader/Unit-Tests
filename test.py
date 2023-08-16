import king
import points as pt
import unittest
import village


class TestKingMovement(unittest.TestCase):
    def setUp(self):
        self.level = 1
        self.V = village.createVillage(self.level)
        self.position = [pt.config["hero_pos"][0], pt.config["hero_pos"][0]]
        self.TestKing = king.spawnKing(pt.config["hero_pos"])
        self.speed = 1

    def tearDown(self):
        pass

    def move_test(self, direction, V):
        if (self.TestKing.alive == False):
            return
        vmap = V.map
        if direction == 'up':
            for i in range(self.speed):
                r = self.position[0] - 1
                c = self.position[1]
                if (r < 0):
                    continue
                if (vmap[r][c] != pt.BLANK and vmap[r][c] != pt.SPAWN):
                    break
                self.position[0] -= 1
        elif direction == 'down':
            for i in range(self.speed):
                r = self.position[0] + 1
                c = self.position[1]
                if (r >= len(vmap)):
                    continue
                if (vmap[r][c] != pt.BLANK and vmap[r][c] != pt.SPAWN):
                    break
                self.position[0] += 1
        elif direction == 'left':
            for i in range(self.speed):
                r = self.position[0]
                c = self.position[1] - 1
                if (c < 0):
                    continue
                if (vmap[r][c] != pt.BLANK and vmap[r][c] != pt.SPAWN):
                    break
                self.position[1] -= 1
        elif direction == 'right':
            for i in range(self.speed):
                r = self.position[0]
                c = self.position[1] + 1
                if (c >= len(vmap[0])):
                    continue
                if (vmap[r][c] != pt.BLANK and vmap[r][c] != pt.SPAWN):
                    break
                self.position[1] += 1

    def test_speed(self):
        self.assertGreater(self.TestKing.speed, 0)

    def test_movement_up(self):
        for i in range(pt.config["dimensions"][0]):
            for j in range(pt.config["dimensions"][1]):
                if (self.V.map[i][j] != pt.BLANK and self.V.map[i][j] != pt.SPAWN):
                    continue
                self.TestKing.alive = True
                self.position[0] = i
                self.position[1] = j
                self.TestKing.position[0] = i
                self.TestKing.position[1] = j
                self.move_test("up", self.V)
                self.TestKing.move("up", self.V)
                self.assertEqual(self.position, self.TestKing.position)

                self.TestKing.alive = False
                self.position[0] = i
                self.position[1] = j
                self.TestKing.position[0] = i
                self.TestKing.position[1] = j
                self.move_test("up", self.V)
                self.TestKing.move("up", self.V)
                self.assertEqual(self.position, self.TestKing.position)

    def test_movement_down(self):
        for i in range(pt.config["dimensions"][0]):
            for j in range(pt.config["dimensions"][1]):
                if (self.V.map[i][j] != pt.BLANK and self.V.map[i][j] != pt.SPAWN):
                    continue
                self.TestKing.alive = True
                self.position[0] = i
                self.position[1] = j
                self.TestKing.position[0] = i
                self.TestKing.position[1] = j
                self.move_test("down", self.V)
                self.TestKing.move("down", self.V)
                self.assertEqual(self.position, self.TestKing.position)

                self.TestKing.alive = False
                self.position[0] = i
                self.position[1] = j
                self.TestKing.position[0] = i
                self.TestKing.position[1] = j
                self.move_test("down", self.V)
                self.TestKing.move("down", self.V)
                self.assertEqual(self.position, self.TestKing.position)

    def test_movement_left(self):
        for i in range(pt.config["dimensions"][0]):
            for j in range(pt.config["dimensions"][1]):
                if (self.V.map[i][j] != pt.BLANK and self.V.map[i][j] != pt.SPAWN):
                    continue
                self.TestKing.alive = True
                self.position[0] = i
                self.position[1] = j
                self.TestKing.position[0] = i
                self.TestKing.position[1] = j
                self.move_test("left", self.V)
                self.TestKing.move("left", self.V)
                self.assertEqual(self.position, self.TestKing.position)

                self.TestKing.alive = False
                self.position[0] = i
                self.position[1] = j
                self.TestKing.position[0] = i
                self.TestKing.position[1] = j
                self.move_test("left", self.V)
                self.TestKing.move("left", self.V)
                self.assertEqual(self.position, self.TestKing.position)

    def test_movement_right(self):
        for i in range(pt.config["dimensions"][0]):
            for j in range(pt.config["dimensions"][1]):
                if (self.V.map[i][j] != pt.BLANK and self.V.map[i][j] != pt.SPAWN):
                    continue
                self.TestKing.alive = True
                self.position[0] = i
                self.position[1] = j
                self.TestKing.position[0] = i
                self.TestKing.position[1] = j
                self.move_test("right", self.V)
                self.TestKing.move("right", self.V)
                self.assertEqual(self.position, self.TestKing.position)

                self.TestKing.alive = False
                self.position[0] = i
                self.position[1] = j
                self.TestKing.position[0] = i
                self.TestKing.position[1] = j
                self.move_test("right", self.V)
                self.TestKing.move("right", self.V)
                self.assertEqual(self.position, self.TestKing.position)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestKingMovement)
    result = unittest.TestResult()
    suite.run(result)
    f = open("output.txt", 'w')
    if result.wasSuccessful():
        f.write("True")
        f.close()
        exit(0)
    else:
        f.write("False")
        f.close()
        exit(1)
