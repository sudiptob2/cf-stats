from app.utils.acronym import Acronym


class TestAcronym:
    """Tests Ancronym handler class."""

    def test_acronymize(self):
        """Tests acronymize with valid parametes."""
        org_name = 'Patuakhali Sceince and Technology university.'
        expected = 'PSTU'
        acc_handler = Acronym()
        actual = acc_handler.acronymize(org_name)
        assert expected == actual

    def test_acronymize_with_acronym(self):
        """Tests acronymize on sentence with acronym."""
        org_name = 'ITMO university.'
        expected = 'ITMOU'
        acc_handler = Acronym()
        actual = acc_handler.acronymize(org_name)
        assert expected == actual

    def test_acronymize_with_long_acc(self):
        """Tests acronymize on long acronym."""
        org_name = 'ITMO University of Science and Technology.'
        expected = 'IT'
        acc_handler = Acronym()
        actual = acc_handler.acronymize(org_name)
        assert expected == actual

