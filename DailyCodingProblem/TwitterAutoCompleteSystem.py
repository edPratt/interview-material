def autocomplete(query_string, all_query_strings):
    """Function that given a query string s and a set of all possible query strings, returns all strings in the set that have prefix s

    Example: autocomplete("de", [dog, deer, deal]) => [deer, deal]
    """
    return [string for string in all_query_strings if (len(string) >= len(query_string) and string[0:len(query_string)] == query_string)]

if __name__ == "__main__":
    print(autocomplete("de", ["dog", "deer", "deal"]))
