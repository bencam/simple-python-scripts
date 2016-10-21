#!/usr/bin/env python


"""Memory is a simple game that can be played by one or more players.
A deck of cards composed of matching pairs is used. The cards are
placed face down and the player or players take turns to try to find
the matching pairs. A turn consists of turning over two cards. If a
match is found, the cards are removed. Otherwise, the cards are
turned face down again. The game ends when all of the matches have
been found.

This version of the game uses capital letters for each card. When a
card is face up, a capital letter is shown. When it is face down, a
single underscore character is shown. A capital X is shown for a spot
where a card has been removed (due to it being matched with another
card). The deck is composed of ten pairs.

NOTE: This script was created as part of a project to build a game
on Google App Engine. The Google App Engine version of this game is
still in progress but will be posted on GitHub in the near future.
"""


import random


def welcome():
    """Print welcome"""
    print ''
    print 'Welcome to Memory!'
    raw_input('Press return to start')
    print ''


def deck_creation():
    """Create a list of 20 cards selected at random"""
    # Create a starting deck of 20 cards
    cards = [
        'A',
        'A',
        'B',
        'B',
        'C',
        'C',
        'D',
        'D',
        'E',
        'E',
        'F',
        'F',
        'G',
        'G',
        'H',
        'H',
        'I',
        'I',
        'J',
        'J']

    # Set variable for a card list to modify
    selection_deck = cards
    # Variable for the deck used in the game
    game_deck = []
    game_deck_counter = 0

    # Build the game deck
    while (game_deck_counter < 20):
        ran_card = random.choice(cards)
        selection_deck.remove(ran_card)
        game_deck.extend(ran_card)
        game_deck_counter += 1
    return game_deck


def show_score(matches, guesses, match_list, match_list_int):
    """Print the current score"""
    print ''
    print 'Here\'s the score:'
    print 'Matches: %s' % matches
    print 'Guesses: %s' % guesses
    print 'Here is the match_list: %s' % match_list
    print 'Here is the match_list_int: %s' % match_list_int  # TESTING
    print ''


def take_a_guess(match_list_int):
    """Returns user input for each guess and prevents a user from
    selecting a card that doesn't exist and prevents a user from
    selecting a card that has already been found in a match"""
    deck_check = range(20)
    guess = int(raw_input('Choose a card to flip over: '))
    while guess not in deck_check or guess in match_list_int:
        if guess not in deck_check:
            print 'Sorry, that\'s not a card in this deck. Try again.'
            guess = int(raw_input('Choose a card to flip over: '))
        elif guess in match_list_int:
            print 'Sorry, there isn\'t a card there. Try again.'
            guess = int(raw_input('Choose a card to flip over: '))
    return guess


def deck_display(disp_deck, guess_int, guess):
    """Display the deck showing only the card that
    was flipped over on the first move"""
    disp_deck[guess_int] = guess
    print disp_deck


def deck_display_match(disp_deck, guess1_int, guess2_int):
    """Display the deck showing a blank spot for cards
    that have been matched"""
    disp_deck[guess1_int] = 'X'
    disp_deck[guess2_int] = 'X'


def reset_deck(disp_deck, guess1_int, guess2_int):
    """Reset the deck so that cards flipped over in the most
    recent turn are flipped back over when the next turn starts"""
    disp_deck[guess1_int] = '_'
    disp_deck[guess2_int] = '_'


def win_or_lose(matches, guesses):
    """Determine if a plaer has won or lost after each turn
    If won or lost conditions are met, function returns true,
    which breaks the keep_playing while loop."""
    # Figure out if the player has won
    if matches == 10:
        print 'You won!'
        print 'It took you %s guesses to win.' % guesses
        return True

    # Figure out if the player has lost
    elif guesses == 30:
        print 'Game over.'
        print 'You\'ve run out of guesses.'
        return True


# Play the game
def play_game():
    """Eexcute a while loop that will run until a player
    has won or lost"""
    keep_playing = True
    deck = deck_creation()
    print 'This is the game deck: %s' % deck  # TESTING
    disp_game_deck = ['_' for x in range(len(deck))]
    match_list = []
    match_list_int = []
    matches = 0
    guesses = 0

    while keep_playing:
        # Print stats
        show_score(matches, guesses, match_list, match_list_int)

        # First guess
        guess1_int = int(take_a_guess(match_list_int))
        guess1 = deck[guess1_int]
        print 'Guess number one int is: %s' % guess1_int  # TESTING
        print 'Guess number one is a: %s' % guess1  # TESTING
        deck_display(disp_game_deck, guess1_int, guess1)

        # Second guess
        guess2_int = int(take_a_guess(match_list_int))
        guess2 = deck[guess2_int]
        print 'Guess number two int is: %s' % guess2_int  # TESTING
        print 'Guess number two is a: %s' % guess2  # TESTING
        deck_display(disp_game_deck, guess2_int, guess2)
        guesses += 1

        # Figure out if it's a match
        if guess1 == guess2 and guess1_int != guess2_int:

            # Find out if the match was already found
            if guess1 not in match_list:
                print 'You found a match!'
                matches += 1
                match_list.extend(guess1)
                match_list.extend(guess2)
                match_list_int.append(guess1_int)
                match_list_int.append(guess2_int)
                deck_display_match(disp_game_deck, guess1_int, guess2_int)
                # Exit the loop if the player won or lost
                if win_or_lose(matches, guesses):
                    keep_playing = False

            else:
                print 'You already found that match.'
                # Exit the loop if the player lost
                if win_or_lose(matches, guesses):
                    keep_playing = False

        elif guess1_int == guess2_int:
            print 'You can\'t pick the same card twice!'
            # Reset the board
            reset_deck(disp_game_deck, guess1_int, guess2_int)
            # Exit the loop if the player lost
            if win_or_lose(matches, guesses):
                keep_playing = False

        else:
            print 'Sorry, you didn\'t find a match.'
            # Reset the board
            reset_deck(disp_game_deck, guess1_int, guess2_int)
            # Exit the loop if the player lost
            if win_or_lose(matches, guesses):
                keep_playing = False


welcome()
play_game()