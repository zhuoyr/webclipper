from webclipper.databases import dbinfo
from webclipper.model.domain import Domain
from webclipper.model.structure import Structure


class Section:
    """
    Show to news the possible pages' structures.

    Attributes:
        url: String with the url of sub-domain.
        structures: List of Pages.
    """

    def __init__(self, url=str()):
        # Define attributes
        self.url = url
        self.domain = Domain()
        self.structures = list()

        # Load pages from database
        self.load_structures()

        # Load domain
        self.load_domain()

    def load_structures(self):
        """ Create and load pages objects from database """
        # Retrieve structures from database
        query = "SELECT * FROM structure " \
                "JOIN section " \
                "ON section.url = structure.section_url " \
                "WHERE section.url = '" + self.url + "';"
        result = dbinfo.select(query)

        # Instance and append each structure to list
        for row in result:
            structure = Structure(row=row)
            self.structures.append(structure)

    def load_domain(self):
        # Retrieve structures from database
        query = "SELECT * FROM domain " \
                "JOIN section " \
                "ON domain.url = section.domain_url " \
                "WHERE section.url = '{url}' " \
                "LIMIT 1;" \
            .format(url=self.url)
        result = dbinfo.select(query)

        for row in result:
            domain = Domain(row=row)

        self.domain = domain
