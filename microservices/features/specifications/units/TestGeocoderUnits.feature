Feature: Unit tests for the geocoding module

  Scenario: Encode
    Given postal address ""
    When  encoded
    Then  coordinates lat=0 lon=0

  Scenario: Decode
    Given coordiantes lat=0 lon=0
    When  decoded
    Then  postal address ""

  Scenario: Matrix
    Given list of locations set ""
    When  all pairs shortest path calculated
    Then  distance matrix for set ""