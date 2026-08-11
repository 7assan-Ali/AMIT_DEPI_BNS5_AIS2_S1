def is_prime(self, num):
        """
        Check whether a number is prime.

        Returns:
            bool: True if the number is prime, otherwise False.
        """

        if num <= 1:
            return False

        for i in range(2, num):
            if num % i == 0:
                return False

        return True