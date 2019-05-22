# Analyze page for desired information


def analyze_general(soup):
    """
    This is meant to analyze a web page in a generic manner (not site-specific)
    Get title
    Get text
        - Manipulate
        - Determine topic
            - Determine keywords
        - Determine how it presents the information
            - article
            - forum
        - Determine if it is a question and whether there is an answer
        - Determine whether the information may be stored in a special manner that makes
          it more difficult to analyze (table, image, etc)
            - Maybe should add image-to-text recognition in order to analyze information
              in such cases
            - use pandas for table analysis
    Save
    :param soup:
    :return:
    """

    print(soup.title.text)
    # print(soup.p.text)

    # getting all text
    # print(soup.get_text())

    # Getting information only from 'body' of page
    # (Enclosed within body tag)
    body = soup.body
    for paragraph in body.find_all('p'):
        print(paragraph.text + "\n")

    # Getting information from table
    table = soup.table
    if table is not None:
        print(table.text)
        # Getting only row data
        table_rows = table.find_all('tr')
        for row in table_rows:
            data = row.find_all('td')
            row_data = [i.text for i in data]
            print(row_data)

    return soup
