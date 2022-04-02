import allure


class Assert:

    @staticmethod
    def equality(
        variable_first,
        variable_second,
        text_error: str,
    ) -> None:
        """Checking for equality of values of two fields (of the same data type)

        :Args:
            variable_first(any): value of the first field
            variable_second(any): value of the  second field
            text_error(str): error text
        """
        with allure.step(
            'Assertion: equality "{}" == "{}"'.format(
                variable_first, variable_second,)
        ):
            try:
                assert variable_first == variable_second
            except:
                assert False, text_error

    @staticmethod
    def inequality(
        variable_first,
        variable_second,
        text_error: str,
    ) -> None:
        """Checking for inequality of values of two fields
        (of the same data type)

        :Args:
            variable_first(any): value of the first field
            variable_second(any): value of the  second field
            text_error(str): error text
        """
        with allure.step(
            'Assertion: inequality "{}" != "{}"'.format(
                variable_first, variable_second,)
        ):
            try:
                assert variable_first != variable_second
            except:
                assert False, text_error

    @staticmethod
    def count_compration(
        variable_large,
        variable_smaller,
        text_error: str,
    ) -> None:
        """Comparing two numeric values

        Args:
            variable_large(any): the value of the larger number
            variable_smaller(any): smaller field value
            text_error(str): error text
        """
        with allure.step(
            'Assertion: comparing "{}" > "{}"'.format(
                variable_large, variable_smaller,)
        ):
            try:
                assert variable_large > variable_smaller
            except:
                assert False, text_error

    @staticmethod
    def contains(
        variable_what,
        variable_where,
        text_error: str,
    ) -> None:
        """Checking the content in something (a in b)

        :Args:
            variable_what(any): what should be contained
            variable_where(any): where it should be contained
            text_error(str): error text
        """
        with allure.step(
            'Assertion: content "{}" in "{}"'.format(
                variable_what, variable_where
            )
        ):
            try:
                assert variable_what in variable_where
            except:
                assert False, text_error
