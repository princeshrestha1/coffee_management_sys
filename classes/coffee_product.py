class Products:
    def __init__(self):
        self.name = []
        self.type = []
        self.cost = []
        self.company = []

    def add_products(self,name, type, cost, company):
        self.name.append(name)
        self.type.append(type)
        self.cost.append(cost)
        self.company.append(company)
        return True

    def show_products(self):
        all_product = []
        for i in range(len(self.name)):
            all_product.append((self.name[i], self.type[i],self.cost[i],self.company[i]))
        return all_product

    def update_products(self):
        pass

    def delete_products(self):
        pass

