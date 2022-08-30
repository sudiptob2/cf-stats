from app.utils.string_utils import Acronym, StringSlicer


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


class TestStringSlicer:
    """Tests StringSlicer class."""

    def test_slice_with_short_name(self):
        """Tests slice with short name string."""
        full_name = 'Sudipto Baral'
        expected = 'Sudipto Baral'
        string_slicer = StringSlicer()
        actual = string_slicer.slice(full_name)

        assert expected == actual

    def test_slice_with_long_name(self):
        """Tests slice with long name string."""
        full_name = 'Shubham kumar Anand'
        expected = 'Shubham'
        string_slicer = StringSlicer()
        actual = string_slicer.slice(full_name)

        assert expected == actual

    def test_generate_appropriate_size_string(self):
        """Tests __generate_appropriate_size_string with name having multiple spaces"""
        full_name = "MD Abdul Rahman Talukder"
        expected = "MD Abdul"
        string_slicer = StringSlicer()
        actual = string_slicer._StringSlicer__generate_appropriate_size_string(full_name)

        assert expected == actual

    def test_generate_appropriate_size_string_with_long_name(self):
        """Tests __generate_appropriate_size_string with long name having no spaces"""
        full_name = "schwarzenegger"
        expected = "schwarzenegger"
        string_slicer = StringSlicer()
        actual = string_slicer._StringSlicer__generate_appropriate_size_string(full_name)

        assert expected == actual
