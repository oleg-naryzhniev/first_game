class Stats():
    """отслеживание статистики"""

    def __init__(self):
        """инициализация статистики"""
        self.reset_stats()
        self.run_game = True
    # максимальный счет убийств
        #self.high_score = 0
        with open('high_score.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """статистика изменяющиеся во время игры"""
        self.guns_left = 2
        self.score = 0