import random


class CrosswordGenerator:
    def __init__(self, words):
        self.words = sorted(words, key=len, reverse=True)
        self.grid = {}
        self.placed_words = []

    def generate(self):
        if not self.words: return []
        self.grid = {}
        self.placed_words = []

        # Putting the parent word at the middle
        self._place_word(self.words[0], 0, 0, 'h')

        # Trying to replace other words
        for word in self.words[1:]:
            self._try_place(word)

        return self.placed_words

    def _place_word(self, word, x, y, direction):
        for i, letter in enumerate(word):
            nx, ny = (x + i, y) if direction == 'h' else (x, y + i)
            self.grid[(nx, ny)] = letter
        self.placed_words.append({
            'word': word, 'x': x, 'y': y, 'direction': direction
        })

    def _try_place(self, word):
        best_positions = []
        for placed in self.placed_words:
            for i, lp in enumerate(placed['word']):
                for j, lw in enumerate(word):
                    if lp == lw:
                        px, py = (placed['x'] + i, placed['y']) if placed['direction'] == 'h' else (placed['x'], placed['y'] + i)
                        new_dir = 'v' if placed['direction'] == 'h' else 'h'
                        nx, ny = (px - j, py) if new_dir == 'h' else (px, py - j)

                        if self._is_valid(word, nx, ny, new_dir):
                            best_positions.append((nx, ny, new_dir))

        if best_positions:
            pos = random.choice(best_positions)
            self._place_word(word, *pos)
            return True
        return False

    def _is_valid(self, word, x, y, direction):
        word_cells = []
        for i in range(len(word)):
            nx, ny = (x + i, y) if direction == 'h' else (x, y + i)
            word_cells.append((nx, ny))

        for i, (cx, cy) in enumerate(word_cells):
            if (cx, cy) in self.grid:
                if self.grid[(cx, cy)] != word[i]: return False
                continue

            neighbors = [(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)]
            for nx, ny in neighbors:
                if (nx, ny) in self.grid and (nx, ny) not in word_cells:
                    return False

        edges = [(x - 1, y), (x + len(word), y)] if direction == 'h' else [(x, y - 1), (x, y + len(word))]
        for ex, ey in edges:
            if (ex, ey) in self.grid: return False

        return True


def get_puzzle_data(raw_words, letters):
    all_valid_words = raw_words

    # Grouping words by their length
    words_by_len = {}
    for w in all_valid_words:
        l = len(w)
        if l not in words_by_len: words_by_len[l] = []
        words_by_len[l].append(w)

    selected_for_grid = []
    # Parent word
    longest_word = max(all_valid_words, key=len)
    selected_for_grid.append(longest_word)

    # Selecting a balanced and random selection of words with 3, 4, 5 or more letters (Max 12 words)
    for l in sorted(words_by_len.keys()):
        if len(selected_for_grid) >= 12: break
        candidates = [w for w in words_by_len[l] if w not in selected_for_grid]
        if not candidates: continue

        # choosing 3 long, 2 short words
        count = 3 if l <= 4 else 2
        picked = random.sample(candidates, min(len(candidates), count))
        selected_for_grid.extend(picked)

    selected_for_grid = selected_for_grid[:12]

    # Placing attempts
    best_result = []
    max_attempts = 45
    for i in range(max_attempts):
        random.shuffle(selected_for_grid)
        gen = CrosswordGenerator(selected_for_grid)
        res = gen.generate()
        if len(res) >= 5:
            if len(res) > len(best_result):
                best_result = res
            if len(res) == len(selected_for_grid): break

    # If app could not find any matches, app returns none
    if not best_result: return {"words": [], "letters": letters, "extraWords": []}

    placed_word_strings = [p['word'] for p in best_result]
    extra_words = [w for w in all_valid_words if w not in placed_word_strings]

    min_x = min(p['x'] for p in best_result)
    min_y = min(p['y'] for p in best_result)
    for p in best_result:
        p['x'] -= min_x
        p['y'] -= min_y

    return {"words": best_result, "letters": letters, "extraWords": extra_words}