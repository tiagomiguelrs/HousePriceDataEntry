class DataConstructor:
    """
    Data constructor dor the scraped address, price and link of an apartment.
    """
    def __init__(self, address: str, price: str, link: str):
        self.address = address
        self.price = price
        self.link = link
