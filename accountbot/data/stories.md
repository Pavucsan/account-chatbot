## account happy path
* ask_reply_fine
 - utter_ask_reply_fine
* greet
    - utter_greet


## account ask question
* ask_reply_fine
 - utter_ask_reply_fine

## account ask help
* account_ask_help
 - utter_account_ask_help

## account help
* account_help
 - utter_account_help

## account account_content
* account_content
 - utter_account_content

## account account
* what_account
    - utter_what_account

## account pinciples
* accounting_principles
- utter_accounting_principles

## account what_are_the_types
* what_are_the_types
- utter_what_are_the_types

## account what_bookkeeping
* what_bookkeeping
- utter_what_bookkeeping

## account accounting_courses
* accounting_courses
- utter_accounting_courses

## account basic_cost_accounting
* basic_cost_accounting
- utter_basic_cost_accounting







## happy path
* ask_reply_fine
 - utter_ask_reply_fine
* greet
  - utter_greet
* mood_great
  - utter_happy


## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
* ask_reply_fine
 - utter_ask_reply_fine
