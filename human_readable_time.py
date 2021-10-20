import tests as t
def main():
    def make_readable(seconds):
        def append_zero(number):
            help_number = str(number)
            if len(str(help_number)) < 2:
                help_number = '0' + help_number
            return help_number

        help_seconds = seconds
        seconds_in_an_hour = 3600
        seconds_in_a_minute = 60

        hours = int(help_seconds / seconds_in_an_hour)
        help_seconds = int(help_seconds - (hours * seconds_in_an_hour))

        minutes = int(help_seconds / seconds_in_a_minute)
        help_seconds = int(help_seconds - (minutes * seconds_in_a_minute))

        return append_zero(hours) + ':' + append_zero(minutes) + ':' + append_zero(help_seconds)

    print(t.assert_equals(make_readable(0), "00:00:00"))
    print(t.assert_equals(make_readable(5), "00:00:05"))
    print(t.assert_equals(make_readable(60), "00:01:00"))
    print(t.assert_equals(make_readable(86399), "23:59:59"))
    print(t.assert_equals(make_readable(359999), "99:59:59"))

if __name__ == "__main__":
    main()
