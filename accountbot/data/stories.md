## account happy path
* ask_reply_fine
 - utter_ask_reply_fine
* greet
    - utter_greet

## happy path
* greet
  - utter_greet
  - utter_account_content
  - utter_your_need

## sad path 1
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## story_thankyou
* thanks
    - utter_noworries

## bot challenge
* bot_challenge
  - utter_iamabot

## acknowledgement
* acknowledgement
- utter_acknowledgement

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
    - utter_more_help

## account pinciples
* accounting_principles
- utter_accounting_principles
- utter_more_help

## account what_are_the_types
* what_are_the_types
- utter_what_are_the_types
- utter_more_help

## account what_bookkeeping
* what_bookkeeping
- utter_what_bookkeeping
- utter_more_help

## account accounting_courses
* accounting_courses
- utter_accounting_courses
- utter_more_help

## account basic_cost_accounting
* basic_cost_accounting
- utter_basic_cost_accounting
- utter_more_help

## New Story acounting

* greet
    - utter_greet
    - utter_account_content
    - utter_your_need
* what_account
    - utter_what_account
    - utter_more_help
* account_content
    - utter_account_content

## New Story accounting ack

* greet
    - utter_greet
    - utter_account_content
    - utter_your_need
* what_account
    - utter_what_account
    - utter_more_help
* basic_cost_accounting
    - utter_acknowledgement

## New Story accounting principle

* greet
    - utter_greet
    - utter_account_content
    - utter_your_need
* accounting_pinciples
    - utter_accounting_principles
    - utter_more_help
