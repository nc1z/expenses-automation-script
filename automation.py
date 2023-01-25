class Automation:
    def __init__(self):
        self.entry_format = ['INPUT_YEAR', 'INPUT_MONTH', 'INPUT_DATE', 'INPUT_LINE_ITEM', 'INPUT_CATEGORY',
                             'INPUT_LINE_ITEM_TYPE', 'INPUT_PAYMENT_TYPE', 'INPUT_AMOUNT', 'INPUT_METHOD', 'INPUT_TIMEFRAME']
        self.x_copy, self.y_copy = None, None
        self.x_paste, self.y_paste = None, None
        self.listener = None
        self.line_items = []
        self.completion_count = 0
        self.line_spacing = 20  # calibrate this to fit your own use case
