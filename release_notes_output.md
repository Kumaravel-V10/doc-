# Release Notes

Date: 2026-08-18
Application Release: Drop 1

## 1. Introduction
This document outlines the features and user stories included in the Drop 1 release of the application. It consolidates user stories and provides detailed acceptance criteria for each item.

## 2. What's New (User Stories)

### Source: Drop1-US

##### US-Offer-35: Offers - Promotional Offer

**Description/User Story:**
I want the system to display if any promotion applied to the flight Offer

**Acceptance Criteria:**
The system must display - visual indicator
- Promotion indicator (Promo Fare)

---

##### US-Offer-36: Offers - Discount Offer

**Description/User Story:**
I want the system to display if any discount applied to the flight Offer

**Acceptance Criteria:**
The system must display - visual indicator
- Discount indicator (Special Offer or Discounted)

---

##### US-Cart-02: Cart - View Flight, Pax & Price details

**Description/User Story:**
I want to view complete details of the flight offer in the cart

---

##### Increment-2 US: 

---

##### Increment-2 US(CRM & ARD Integration): 

---

#### Feature: F1.1 - SC_F2_1//Search Criteria_Offer Search

##### US-Config-01: Support Airline-specific Origins

**Description/User Story:**
I want the system to support a list of origins marked by the airline

**Acceptance Criteria:**
If the airline marks a list of origins, then the system must support this list when providing origin options to the user.

If an administrator configures origins  via the admin interface, then the system must reflect these changes in the user interface.

If an agent selects an origin and destination for OW (One Way) or RT (Round Trip) itineraries, then the system must ensure these are different locations.

• Can be determined whether its of location type "Airport" or "City"
• The Locations in the autosuggest are presented in the following format:
<city> - <airport> (<airport code>),<state>, <country>

---

##### US-Config-02: Support Airline-specific Destinations

**Description/User Story:**
I want the system to support a list of destinations marked by the airline

**Acceptance Criteria:**
If the airline marks a list of destinations, then the system must support this list when providing origin options to the user.

If an administrator configures destinations via the admin interface, then the system must reflect these changes in the user interface.

If an agent selects an origin and destination for OW (One Way) or RT (Round Trip) itineraries, then the system must ensure these are different locations.

• Can be determined whether its of location type "Airport" or "City"
• The Locations in the autosuggest are presented in the following format:
<city> - <airport> (<airport code>),<state>, <country>

---

##### US-Config-03: Support Airline-specific Cabin Types

**Description/User Story:**
I want the system to support search for all cabin classes marketed by the airline
- Agent can apply Cabin filters on customer request

**Acceptance Criteria:**
• The system must support search for one or all cabin classes.
Cabin classes must be configurable via the admin interface

---

##### US-Config-04: Support Airline-specific Fare Families per Cabin Types

**Description/User Story:**
I want the system to support configuration of Fare Familes per cabin classes marketed by the airline

---

##### US-Config-05: Support Airline-specific Trip Types

**Description/User Story:**
I want the system to support a list of Trip types marked by the airline
- Agent can apply configured Trip types based on the customer request

**Acceptance Criteria:**
Iteration 1: Supported Trip Type is One way (OW) & Return (RT)
OW - 1 set of flight & Return date field is hidden or disabled 
RT - 2 sets of flight Outbound & Inbound. Return date is must

---

##### US-Config-06: Support Airline-specific Point of Sale (PoS)/ Market

**Description/User Story:**
I want the system to support a list of Market/ PoS marked by the airline

I want the system to retrieve allowed origins and destinations based on the Point of Sale (POS)/ market

**Acceptance Criteria:**
• The system must retrieve allowed origins and destinations based on the POS.
• The system must have the capability to exclude certain Origins and Destinations for a PoS.

---

##### US-Config-07: Support Airline-specific CFF

**Description/User Story:**
I want the system to support a list of CFF marked by the airline
- Agent can apply CFF configured in the system during search

**Acceptance Criteria:**
Airline can configure list of CFFs per PoS/ Market

If an agent selects an Origin or PoS/ Market for any Trip Type, then the sytem has to provide the list of CFFs for the agent to select

---

##### US-Config-08: Support Airline-specific Frequent Flyer Program

**Description/User Story:**
I want the system to support a list of Frequent Flyer Program needed by the airline
- Agent can choose a configured Frequent Flyer Program on the customer preference/ request

**Acceptance Criteria:**
Support Frequent flyer program selection

---

##### US-Config-09: Support Airline-specific Language

**Description/User Story:**
I want the system to support a list of Languages needed by the airline
- Agent can choose a language configured in the system

**Acceptance Criteria:**
Support language selection 
Available languages - EN, …
All labels, error message and dynamic content adapt based on the selected language

---

##### US-Config-10: Support Airline-specific Currency

**Description/User Story:**
I want the system to handle searches based on currency
- Agent can choose a configured currency based on the customer request

**Acceptance Criteria:**
• The system must accept currency parameters in the shopping request.
• The system must return flight prices in the specified currency
Supported Currency: EUR, USD, …
 - Currency  changes update prices dynamically across the shopping flow

---

##### US-Config-11: Support Airline-specific Operating Carriers

**Description/User Story:**
I want the system to support a list of Operating Carrier needed by the airline
- Agent can filter flights based on the operating carrier

**Acceptance Criteria:**
The system allows filtering search results based on the Operating Carrier
Increment 1: Only Finnair Marketed & Operated flights

---

##### US-Config-12: Support Airline-specific Shopping Types

**Description/User Story:**
I want the system to support a list of Shopping Types needed by the airline

**Acceptance Criteria:**
Airline can configure possible Shopping types - Revenue, Group, Staff, Corporate,...

---

##### US-Config-13: Support Airline-specific Passenger Type codes with Age range

**Description/User Story:**
I want the system to support a list of Passenger Types (PTC) with Age definition marked by the airline
- Agent can select configured/ apply different PTCs in the search
- System can validate PTC age in the Passenger Information section

**Acceptance Criteria:**
If the airline marks a list of PTCs with configured age definitions, then the system must support this list when providing Passenger Types options to the user.

The system must ensure to validate the age of the PTC based on the Date of the Birth input in the Passenger details.

Iteration 1: Supported PTCs are ADT, CHD, INF
Age range can be overrideable per Airline
PTC age range is configurable.

---

##### US-Config-14: Support Airline-specific Passenger Type code with Discount Code

**Description/User Story:**
I want the system to support a list of Discount codes per Passenger Types (PTC) defined by the airline
- Agent can apply configured Discount code for a PTC during search
- additionally can validate Discount code of PTC

**Acceptance Criteria:**
If the airline configure list of Discount codes per PTC, then the system must support this discount codes for the respective Passenger Types to the user.

The system must ensure to validate the Discount Code of the PTC based on the configurations

Iteration 1: Supported PTCs are ADT, CHD, INF
Discount codes: MIL,...

---

##### US-Config-15: Support Airline-specific
No of Passengers count

**Description/User Story:**
I want the system to support Search Offer requests for up to configured number of passengers

**Acceptance Criteria:**
If the Airline configures the maximum number of Passenger based on PTC & combinability of other PTCs, then the system must support providing the number the PTCs to the user.

If the number of passengers is entered in the search request exceed the count (more than configuration), then the system must return an error

Note: Configurable should be flexible to support multiple PTCs
The system should limit the count of passenger as per business rules (Refer BR001 & BR004)

---

##### US-Search-01: Flight Search - 1 or more ADT PTCs

**Description/User Story:**
I want the system to search flight offers for 1 or more ADT passenger types

**Acceptance Criteria:**
If the Agent selects 1 or more Passenger Type, then the system must create and price offers for each PTC according to airline-configured age definitions

If an infant passenger (INF) is included, then the system must ensure the infant is associated with an adult (ADT).

---

##### US-Search-02: Flight Search - 1 or more ADT and CHD PTCs

**Description/User Story:**
I want the system to create and search offers for 1 or more ADT along with Child (CHD) passengers

---

##### US-Search-03: Flight Search - 1 or more ADT and INF PTCs

**Description/User Story:**
I want the system to create and search offers for 1 or more ADT along with Infant (INF) passengers

---

##### US-Search-04: Flight Search - 1 or more ADT, CHD and INF PTCs

**Description/User Story:**
I want the system to create and search offers for 1 or more ADT along with Child (CHD) and Infant (INF) passengers

---

##### US-Search-05: Flight Search - One Way (OW)

**Description/User Story:**
I want the system to offer and search One-Way (OW) itineraries

**Acceptance Criteria:**
If a search is submitted, then the request must contain the passenger type and count, and validate that all required parameters (Origin, Destination, Passenger type and count, Travel date) are present.

If any required parameter is missing or invalid, then the system must return an appropriate error message to the user.

If the search criteria match available flights, then the system must return all suitable flight offers for the specified date; when no flights are found, a meaningful message must be displayed.

---

##### US-Search-06: Flight Search - Return (RT)

**Description/User Story:**
II want the system to offer and search Return (RT) and Day Trip itineraries

---

##### US-Search-07: Flight Search - PTC Discount code

**Description/User Story:**
I want to include a passenger type discount code during flight search

**Acceptance Criteria:**
If a discount code is entered against a Passenger Type Code (PTC), then the system must validate the discount code for the PTC. Refer

System provides an optional field to enter the discount code against PTC.

---

##### US-Search-08: Flight Search - 1 or max 3 CFFs applied

**Description/User Story:**
I want to include a specific Commercial Fare Family (CFF) in the search criteria

**Acceptance Criteria:**
If the CFFs are included in the Search, then the system must apply the CFF logic and return relavant/ discounted fare familes; when not specified, all offers are returned by default.

Note: Maximum of 3 CFFs can be applied in the Search. Refer BR006

---

##### US-Search-09: Flight Search - Frequent Flyer Number/ details

**Description/User Story:**
I want to capture frequent flyer program & number for each passengers before search and then initiate search

**Acceptance Criteria:**
If a frequent flyer number is provided, then the system must validate its format and retrieve personalized offers accordingly; when not provided, standard offers are shown. Refer

---

#### Feature: F1.10 - SC_F2_10//Passenger_Information_details_(Contact,_Name,_FF_Numbers,…)

##### US-PaxInfo-01: Pax Info - Pax Info Details

**Description/User Story:**
I want the system to allow agent to enter information for each passenger in the booking.

**Acceptance Criteria:**
* The system must provide fields to enter passenger details such as name (first, middle, last), title, gender. 
 * The system should allow adding information for the number of passengers selected in the previous flight selection step

---

##### US-PaxInfo-02: Pax Info - Contact Details

**Description/User Story:**
I want the system to allow me to enter contact details for at least one adult passenger.

**Acceptance Criteria:**
* The system must provide fields to enter contact details such as phone number and email address. 
 * The system must ensure that contact details are captured for at least one adult passenger 
 * The system should allow capturing contact details for other passengers.

---

##### US-PaxInfo-03: Pax Info - Emergency Details

**Description/User Story:**
I want the system to allow me to enter 1 or more Emergency contact details

---

##### US-PaxInfo-04: Pax Info - Passport Information

**Description/User Story:**
I want the system to allow me to enter passport information for passengers when required.

**Acceptance Criteria:**
* The system must provide fields to enter passport details such as passport number, issuing country, and expiry date. 
 * The requirement for passport information should be configurable per airline

---

##### US-PaxInfo-05: Pax Info - Travel Visa Information

**Description/User Story:**
I want the system to allow me to enter travel visa information for passengers when required.

**Acceptance Criteria:**
* The system must provide fields to enter visa details such as visa number, issuing country, and expiry date. 
 * The requirement for visa information should be configurable per airline.

---

##### US-PaxInfo-06: Pax Info - National ID Information

**Description/User Story:**
I want the system to allow me to enter National ID information for passengers when required.

**Acceptance Criteria:**
* The system must provide fields to enter National ID details such as ID number and issuing country. 
 * The requirement for National ID information should be configurable per airline.

---

##### US-PaxInfo-07: Pax Info - Validation

**Description/User Story:**
I want the system to perform basic validation on the entered passenger information based on the configuration - PTC Age limit, Email address, Mobile regular expression per country code

**Acceptance Criteria:**
* The system must validate the format of the phone number. 
 * The system must validate the format of the email address. 
 * The system must validate the date of birth based on the passenger type (Adult1 , Child3 , Infant4 ) and airline configuration. 
 * The system must validate the selection of a title for each passenger.

---

##### US-PaxInfo-08: Pax Info - Field Configuration

**Description/User Story:**
As an Airline Administrator, I want to be able to configure which passenger information fields are mandatory, optional and required validation regular expressions
Note: Fields could vary per Airline

**Acceptance Criteria:**
* The system must provide an administrative interface to configure mandatory passenger information fields. 
 * Mandatory fields should be configurable at the airline level. 
 * The system must prevent the agent from proceeding if mandatory fields are not completed.

---

##### US-PaxInfo-09: Pax Info - Modify Pax details

**Description/User Story:**
I want to modify the passenner contact in the contact

**Acceptance Criteria:**
System should provide an option to modify the passenger contact details  
(Add New, Delete Existing Contact, Change the existing contact)
Contact Details include - Phone, Email, Address

---

##### US-PaxInfo-10: Pax Info - Retain Paxs details

**Description/User Story:**
I want the system to retain passenger and contact details when modifying offers

**Acceptance Criteria:**
Passenger data should persist in the cart unless incompatible with new offer
Cart must preserve FFN, PTC, Contact Info, Regulatory Doc

---

##### US-PaxInfo-11: Pax Info - Loyalty info

**Description/User Story:**
I want to add loyalty Program & its number

**Acceptance Criteria:**
For each Passenger:
- List of eligible Loyalty Programs are shown (as per configuration)
- Input field with loyalty number

Validate format per Airline Loyalty Program
Recognize tier level per Airline Loyalty Program (Not in Scope)

---

##### US-PaxInfo-12: Pax Info - Infant association

**Description/User Story:**
I want to assign an Infact to an Adult passenger

**Acceptance Criteria:**
One Infant per Adult passenger
If number of Infants exceeds number of Adult - show error

---

##### US-PaxInfo-13: Pax-Info - Bulk Upload of Pax Info via CSV or AI

**Description/User Story:**
I want the system to present an option to bulk upload passenger information & contact details

---

#### Feature: F1.13 - SC_F2_14//Notify_Order_Confirmation

##### US-OrderConfirm-08: Order Confirmation - Send

**Description/User Story:**
As an agent, I want to have quick action buttons to print, email or SMS the order confirmation.

**Acceptance Criteria:**
*The Agent should see the checkboxes to select multiple ways for sending itinerary information to the passenger

---

##### US-OrderConfirm-09: Order Confirmation - Print

**Description/User Story:**
As an agent, I want to print the order details after successful booking.

**Acceptance Criteria:**
*Agent can click on Print Order from order view page.
*System generates printable/PDF  with required PNR,Flight details, pax details and ancillary services if any.
*System allows selection of printer and print settings

---

##### US-OrderConfirm-10: Order Confirmation - Email

**Description/User Story:**
As an agent, I want to send the order confirmation via email to the passsenger.

**Acceptance Criteria:**
*Agent can click on "Send Email" from the order view page,
*System auto-fills the email id, if available
*System provides an option to add or edit the email address
*System sends email itinerary and ancillary services if any

---

##### US-OrderConfirm-11: Order Confirmation - SMS

**Description/User Story:**
As an agent, I want to send the order confirmation via SMS to the passsenger.

**Acceptance Criteria:**
*Agent can click on "Send SMS" from the order view page,
*System auto-fills the phone number, if available
*System provides an option to add or edit the phone number
*System sends SMS itinerary and ancillary services if any

---

#### Feature: F1.19-SC_F2_4-Integrate_with_CRM_Platfom.

##### US-CRM-01: Automatic Agent authentication in SCUI

**Description/User Story:**
As a service center agent, 
I want to be automatically authenticated when accessing SCUI from CRM

**Acceptance Criteria:**
Agent is already authenticated in CRM.
When the agent navigates from CRM to SCUI, no additional login prompt is shown.
SCUI validates the agent’s authentication using SSO.
Agent lands directly on the SCUI successfully.
If the CRM session is invalid or expired, the agent is prompted to authenticate.
CRM and ARDWeb integration need to work seamlessly.

---

##### US-CRM-02: Launch Service Center UI from CRM

**Description/User Story:**
As a contact center agent
I want to launch the Offer-Order based Service Center UI from within CRM

**Acceptance Criteria:**
User can launch SCUI directly from the CRM.
SCUI opens in a new tab or embedded view as per configuration.
User sees an error message if SCUI launch fails.

---

##### US-CRM-03: Auto-populate customer details from CRM

**Description/User Story:**
As a service center agent
I want customer details to be auto-populated in the Service Center UI (SCUI) from the CRM.

**Acceptance Criteria:**
SCUI automatically retrieves customer details from CRM when a customer record is identified. 
Key customer fields (e.g., First name, Lastname, Email, Phone, Frequent flyer number) are populated without manual input. 
Agent should be able to edit autopopulated data.
System handles missing or unavailable CRM data gracefully with a clear message.
Data retrieval follows security and data governance rules.

---

##### US-CRM-04: Create Booking in SCUI Using CRM Customer Data

**Description/User Story:**
As a service center agent
I want the Service Center UI (SCUI) to create a booking using customer details retrieved from CRM.

**Acceptance Criteria:**
SCUI can fetch customer details (e.g., first name, last name, contact details) from CRM.
Retrieved CRM customer data is auto-populated in the booking creation form in SCUI.
Agents can review and edit customer details before confirming the booking.
Booking can be successfully created in SCUI using the CRM-provided customer data.
An error message is displayed if CRM data retrieval fails or is incomplete.

---

##### US-CRM-05: Handle Missing or Partial Customer Details from CRM

**Description/User Story:**
As a service center agent
I want the system to handle missing or partial customer details retrieved from CRM.

**Acceptance Criteria:**
If customer details from CRM are missing or incomplete, the system shall display a clear indicator or message to the user.
The system shall allow manual entry or update of missing customer information where permitted.
Mandatory fields shall be validated before saving or proceeding
The system shall not fail or block the flow due to partial CRM data.

---

#### Feature: F1.2 - SC_F2_2//Display_offers

##### US-Offer-01: Offers - No Offers Found

**Description/User Story:**
I want the system to display message - when no offers are found for a given search criteria

**Acceptance Criteria:**
If no matching flights are found, the system must include return message
 - "No Offer found for given search criteria"

---

##### US-Offer-02: Offers - View Flight Details 

**Description/User Story:**
I want the system to display detailed flight information, Cabin & Fare family details in the Offer/ bound

**Acceptance Criteria:**
If Offer are found, then flight details are presented to the agent must include 
- Date
- Departure time & Origin
- Arrival time & Destination
- Flight number,  Aircarft Type, Operating Carrier,...
- Trip Duration, Leg Duration, Leg Connecting time, Stop Over,...

Refer: FlightDetails

---

##### US-Offer-03: Offers - View Cabin Details 

**Description/User Story:**
I want to compare Cabin types with their respective details  - Prices, terms & conditions, services,..

**Acceptance Criteria:**
If Offer are found, then cabin details are presented to the agent must include
- Cabin Type: Economy, Premium Economy, Business, First Class (as configured by Airlines)
Each Cabin can contain multiple Fare Families (as per configuration)

If Cabin is sold-out
- Sold-Out indicator on the specific Cabin is shown for the Agent

---

##### US-Offer-04: Offers - View Fare Familes Details

**Description/User Story:**
I want to compare Fare Family types with their respective details - Prices, terms & conditions, services,..

**Acceptance Criteria:**
If Offer are found, then Fare Family details are presented to the agent must include
- List of Fare Familes per Cabin: Eco Light, Eco Comfort, Eco Flex (as configured by Airlines)
- Amentites
- List of Services
- Terms & Conditions

If a Fare Family is sold-out
- Sold-Out indicator on the specific Fare family is shown for the Agent

---

##### US-Offer-05: Offers - Included Service details per Offer

**Description/User Story:**
I want the system to display the list of services included in the Offer per Bound

**Acceptance Criteria:**
If Offer are found, then list of Service details are presented to the agent must include (Fare family contain list of entitled Services)
- Checked in Bags or Carry Bags
- Seat Selection
- Lounge, Meal,...

Note: Service details vary per PTC

---

##### US-Offer-06: Offers - Amentities per Flight in the Offer

**Description/User Story:**
I want the system to display the list of Amentities or Special features included in the flight

**Acceptance Criteria:**
If Offer are found, then list of Amenties details are presented to the agent must include per Flight
- Wifi, In Seat Power, ...

---

##### US-Offer-08: Offers - Access detailed Fare rules & benefits/ Mini-Rules

**Description/User Story:**
I want the system to provide access to the detailed fare rules/ condition/ mini-rules will display benefits details for the agent
F1.86 - Fare rules [TODO]
F1.32 - Mini rules [TODO]

**Acceptance Criteria:**
For each flight offer, the system must provide a mechanism (e.g., a link or button) to access the detailed fare rules as provided by the airline.

---

##### US-Offer-09: Offers - View Multiple Offers

**Description/User Story:**
I want the system to display multiple flight Offers

**Acceptance Criteria:**
Comparision in a tabular format showing
- Flight times, Duration, Fare details, Prices,….

---

##### US-Offer-10: Offers - Limited Seats

**Description/User Story:**
I want the system to display limited seats indicator

**Acceptance Criteria:**
If seat availability is low, then an indicator with the available seats is displayed

---

##### US-Offer-11: Offers - Stop Over Information

**Description/User Story:**
I want the system to return flight stop over information for a multi-leg bound

**Acceptance Criteria:**
If Offer has a multiple flight legs details are presented to the agent must include
- Stop overs details: Connecting time, Leg Duration, Trip Duration,...

---

##### US-Offer-12: Offers - Next Day Arrivals

**Description/User Story:**
I want the system to inform when a flight arrives on the next calendar day

**Acceptance Criteria:**
For flights that arrive on the next calendar day 
- Indicate with +1 or time (+1)

---

##### US-Offer-13: Offers - Overnight Layovers

**Description/User Story:**
I want the system to inform when a flight includes an overnight layover

**Acceptance Criteria:**
For connecting flights with Overnight layovers
- Provide an Indicator

---

##### US-Offer-14: Offers - Total Price

**Description/User Story:**
I want the system to clearly display total price for each flight offer

---

##### US-Offer-17: Offers - How many Paxs are being priced

**Description/User Story:**
I want to know how many passengers are being priced and how total fare is calculated

**Acceptance Criteria:**
The system must display
- Number of Passenger & PTCs
- Fare per PTC
- Combined Total for all Passenger

Any discounts (Infants, Child discount,…) must be also listed

---

##### US-Offer-18: Offers - Discount Code (ADT - MIL)

**Description/User Story:**
I want the system to display if any discount applied to the flight Offer based on the PTC discount code

**Acceptance Criteria:**
The system must display
- Discount amount or percentage
- Discount must appear as a separate line in the price breakdown

---

##### US-Offer-19: Offers - Miles info

**Description/User Story:**
I want to see and compare how many miles customer will earn for a specific flight offer

**Acceptance Criteria:**
The system will display miles/ points earned based on Fare family

---

##### US-Offer-20: Offers - Change Currency (for Display only or Sell?)

**Description/User Story:**
I want the system to allow me to change the displayed currency of the flight offers (as per configuration)

**Acceptance Criteria:**
The system must provide an option to change the displayed currency from a list of currencies configured for the Point of Sale. 
The flight offer prices must be updated to the selected currency.

---

##### US-Offer-21: Offers - Offer Time Limit

**Description/User Story:**
I want the system to display an Offer time limit/ Expiration counter or the validity time for each flight offer

**Acceptance Criteria:**
For each flight offer, the system must display either a countdown timer indicating the remaining time the offer is valid or a specific date and time by which the offer expires.

---

##### US-Offer-22: Offers - Offer has Expired

**Description/User Story:**
I want the system to automatically detect and notify when a displayed flight offer has expired

**Acceptance Criteria:**
* Once offer timelimit has reached, the offer status in the should be marked as Expired
*The system should prevent the cart creation process for expired items
*System should provide option to refresh the search results to retrieve new offers

---

##### US-Offer-23: Sort Offers - Best Match

**Description/User Story:**
I want the system to sort flight offers by the airline's definition of best match

**Acceptance Criteria:**
The system must sort flight offers based on a pre-configured "Best Match" algorithm determined by the Amadeus APIs.
Best match must be displayed based on "ranking" field in Amadeus response.

---

##### US-Offer-24: Sort Offers - Departure time

**Description/User Story:**
I want to sort flight offers by departure time

**Acceptance Criteria:**
The system must allow sorting of flight offers based on the departure time for each bound. (Both Ascending and Descending).

---

##### US-Offer-25: Sort Offers - Arrival time

**Description/User Story:**
I want to sort flight offers by arrival time

**Acceptance Criteria:**
The system must allow sorting of flight offers based on the arrival time for each bound. (Both Ascending and Descending)

---

##### US-Offer-26: Sort Flight Offers - Total Price

**Description/User Story:**
I want to sort flight offers by total Price

**Acceptance Criteria:**
The system must allow sorting of flight offers based on the total price of all passengers. (Both Ascending and Descending)

---

##### US-Offer-27: Sort Flight Offers - Duration

**Description/User Story:**
I want to sort flight offers by Duration

---

##### US-Offer-28: Filter Flight Offers - No of Stops

**Description/User Story:**
I want to filter flight offers by Number of Stops

**Acceptance Criteria:**
Filter options include - Nonstop, 1 Stop, …
The Offers must reflect dynamically

---

##### US-Offer-29: Filter Flight Offers - Price Range

**Description/User Story:**
I want to filter flight offers by Price range

**Acceptance Criteria:**
Display price slider

---

##### US-Offer-30: Filter Flight Offers - Time Window (local time)

**Description/User Story:**
I want to filter flight offers by departure and arrival time window

**Acceptance Criteria:**
Time filters
- Departure time (6 am-12pm)
- Arrival time (4pm-6pm)

---

##### US-Offer-31: Filter Flight Offers - Duration

**Description/User Story:**
I want to filter flight offers by total travel duration

**Acceptance Criteria:**
Duration filter with an option to choose maximum travel time

---

##### US-Offer-32: Filter Flight Offers - Cabin

**Description/User Story:**
I want to filter flight offers by cabin class

**Acceptance Criteria:**
Filter by Cabin

---

##### US-Offer-33: Filter Flight Offers - Fare Family

**Description/User Story:**
I want to filter flight offers by departure and arrival time window

**Acceptance Criteria:**
Filter by Fare Families

---

##### US-Offer-34: Filter Flight Offers - Clear all Filter

**Description/User Story:**
I want to clear all applied filters at once

**Acceptance Criteria:**
Option to reset all filters

---

#### Feature: F1.25 - SC_F2_33//Terms_&_Conditions/_Fare_Rules__31,_33,_5,_6,_7

##### US-Offer-07: Offers - Terms & Conditions per Offer

**Description/User Story:**
I want the system to display the list of Terms & Conditions included/ associated with each flight Offer per Bound

**Acceptance Criteria:**
If Offer are found, then list of Terms & Condition details are presented to the agent must include
- Change policies, Penalties
- Refund and cancellation policies
- No Show Policy
- Baggage Allowance
- Restrictions,...

Note: Terms & Conditions can vary per PTC

---

#### Feature: F1.26 - SC_F2_34//Baggage_Policy_details

##### US-BagPolicy01: FBA - View the  Check in Baggage Allowance

**Description/User Story:**
As an Airline Agent,
I want to view the check in baggage policies based on the selected offer(s)

**Acceptance Criteria:**
1. Agent can see the free check-in baggage allowance based on the selected offer.
2. Baggage allowance information is displayed clearly on the booking summary.
3. The system updates baggage allowance automatically if the booking cabin or route changes.

* Display the Free Check-in Baggage allowance applicable for the cart contents with policy details and baggage specifications
* Show the policy applicability per passenger per segment.

---

##### US-BagPolicy02: FBA - View the  Carry on  Baggage Allowance

**Description/User Story:**
As an Airline Agent,
I want to view the carry on baggage policies based on the selected offer(s)

**Acceptance Criteria:**
1. Agent can see the allowed number of carry-on bags for the selected offer.
2. Agent can see the allowed weight and/or dimensions for carry-on bags.
3. Information is displayed clearly on the Order summary or baggage section.
4. Carry-on Baggage allowance differs by Cabin and PTC , the correct allowance should be displayed based on the Offer selected. 

*Display the Free carry on Baggage allowance applicable for the cart contents with policy details and baggage specifications
*Show the policy applicability per passenger per segment.

---

#### Feature: F1.3 - SC_F2_3//Select_Offer

##### US-Cart-01: Cart - Add Flight Offer(s)

**Description/User Story:**
I want the system to add the selected flight offers into a cart

**Acceptance Criteria:**
Cart section must display
- Full Itinerary (dates, times, airlines, duration,…)
- Fare summary & rules per PTC
- Passenger Count
- Taxes and Fees breakdown
- Combined Total cost

Iteration 1: Support OW & RT Trip type

---

##### US-Cart-03: Cart - Modify Flight Offer

**Description/User Story:**
I want to change the selected flight Offer in the cart

**Acceptance Criteria:**
Agent selects a new flight offer from the Flight Offer page
- Removes the old flight offer
- Adds the new flight offer to the cart
- Updates total pricing and itinerary

---

##### US-Cart-04: Cart - Remove Flight Offer

**Description/User Story:**
I want to remove a flight Offer in the cart

**Acceptance Criteria:**
Remove option to each flight offer in the cart

---

##### US-Cart-05: Cart - Flight Offer Time Limit

**Description/User Story:**
I want the system to display an Offer time limit/ Expiration counter or the validity time for each flight offer

---

##### US-Cart-06: Cart - Expired Flight Offer

**Description/User Story:**
I want the system to automatically detect and notify when a displayed flight offer has expired

**Acceptance Criteria:**
* Once offer timelimit has reached, the offer status in the should be marked as Expired
*The system should prevent the cart creation process for expired items
*System should provide option to refresh the search results to retrieve new offers

---

##### US-Cart-07: Cart - Validate (Refresh)

**Description/User Story:**
I want the system to refresh/ validate the cart in realtime for any offer selection, adding pax details,...

**Acceptance Criteria:**
System should return old and current price info on cart repricing
Given a cart undergoes repricing,
When repricing is completed,
Then the cart response must include the following for each cart item (excluding taxes and fees): previous_price, current_price,  price_difference, price_change_type (values: higher, lower, same)

---

##### US-Cart-08: Cart - Validate Cart before Checkout

**Description/User Story:**
I want the system to validate flight Offers before Checkout

**Acceptance Criteria:**
Availability & Fare is checked by the system via Amadeus APIs

---

##### US-Cart-09: Cart - Add Pax Information

**Description/User Story:**
I want the system to add Paxs information to the cart

**Acceptance Criteria:**
System can show all previous entered passenger details in the cart summary

---

##### US-Cart-10: Cart - Update Pax Information

**Description/User Story:**
I want the system to update Paxs information to the cart 
- Update/ Edit the Paxs information in the cart

**Acceptance Criteria:**
Agent can click 'edit' to modiy any field
- Validation rules apply again upon editing
- System shows a success confirmation once data is updated

---

##### US-Cart-11: Cart - Reprice in new Currency

**Description/User Story:**
An agent has added items to their cart while browsing in USD. Before adding anything else, they manually change their selected currency to EUR to view the cart totals in that currency

**Acceptance Criteria:**
Given a request has been made to change the cart’s currency,
When the system processes the currency update,
Then all items currently in the cart must be repriced to reflect the new currency selection

---

##### US-Cart-12: Cart - Clear Cart 

**Description/User Story:**
I want the system to clear the cart once the Order has been sucessfully created

**Acceptance Criteria:**
Given an cart,
When an order is created from the cart
Then clear the cart

---

#### Feature: F1.4-SC_F2_4//Search_ancillaries
F1.9 - SC_F2_9//Special_Assistance,_Free_Services

##### US-Config-16: Configure- Configuration of SSRs by Category

**Description/User Story:**
As a System Administrator, 
I want to maintain a configuration table that maps SSRs to their respective categories

**Acceptance Criteria:**
1. The system shall allow adding new SSR codes with their associated categories.
2. The system shall allow updating category details for existing SSR codes.
3. The system shall prevent duplicate SSR code entries.
4. The system shall allow deleting SSR code entries if no longer required.
5. The configuration table shall be accessible to authorized users only.

---

##### US-Config-17: Configure- Configuration to filter services for PTC

**Description/User Story:**
As a System Administrator, 
I want to maintain a configuration table that maps eligible services to passenger type codes (PTCs)

**Acceptance Criteria:**
1. The configuration table allows administrators to assign each ancillary/service to one or more PTCs (e.g., Adult, Child, Infant).
2. Only services mapped to the specified PTC are shown to agents.
3. The system ensures that services excluded for a PTC are never displayed or selectable for that passenger type.
4. Administrators can edit, add, or remove PTC mappings for services in the configuration table.
5.  The configuration supports real-time updates or updates on next system refresh.

---

##### US-Config-18: Configure- Services Grouping Mechanism (Configurable)

**Description/User Story:**
As a System Administrator, 
I want the system to provide an ability to Group the Services logically

**Acceptance Criteria:**
1. Logical Grouping
•	Services should be grouped at two levels: 
o	Category Level (e.g., Meals, Baggage, Additional Services)
o	Sub-category/Service Level (e.g., Extra Baggage, Heavy Baggage, Sports Equipment under Baggage)
•	Grouping logic should follow airline-defined configuration.

2. Configurable Logic
•	Admin should be able to configure: 
o	Categories and sub-categories.
o	Which services belong to which group.

3. Display Indicator Active/Inactive
•	Each service should have an Active/Inactive status.
•	If a service is Inactive, it should not be displayed on the UI.
•	Make the services disabled automatically if Category is disabled in quick access and custom view
•	Enable/disable the services individually when the category is enabled/disabled

4. Display Order
•	Ability to configure the order of categories and services.
•	UI should display services in the configured order.

5. Quantity & Capacity
•	Each service should have: 
o	Quantity selection (where applicable).
o	Maximum capacity limit (where applicable)
•	If maximum capacity is reached: 
o	Display “Service not available” message.
o	Disable further selection.
o	Refer to BR009, BR010

6. Offered Level
•	Services should be offered at: 
o	Bound level (specific flight segment).
o	Flight level.
•	UI should reflect the correct level based on configuration.

---

##### US-RetrieveAnc-01: RetrieveAnc-  Retreive Ancillaries from catalogue

**Description/User Story:**
As an Airline Agent,
I want to retrieve  all  ancillary services from the service catalogue for a given cart reference.

**Acceptance Criteria:**
1. The system shall allow retreive all ancillaries using a valid Cart reference ID. 
2. The retreive results should display all available ancillaries from the service catalogue applicable to that cart.
3. Each ancillary must include type, description, price, Quota based on API.
4. The results should reflect eligibility based on cart details (e.g., passenger type, flight Id etc.).
5. If no ancillary services are available for the cart, the system should display a clear message:“No ancillary services exists”.

*Disclaimer: Error meesage will be covered in test scenarios.

---

##### US-RetreiveAnc-02: RetreiveAnc - Group Ancillaries based on Category

**Description/User Story:**
I want Service Center UI should have the capability to Group ancillaries based on their categories.

**Acceptance Criteria:**
1. Ancillaries shall be grouped under predefined categories (e.g. Baggage, Seat, Meals, Insurance, etc.).
 2. The system should display grouped ancillaries in a structured format.
3. Each ancillary must belong to at least one category.
4. The airline agent should be able to view all categories and their respective ancillaries.
5. Categories and their order should follow configuration defined by the airline.

---

#### Feature: F1.5-SC_F2_5//Display_&_Select_Ancillary

##### US-SelectAnc-02: SelectAnc - Specify Ancillary Quantity  during selection

**Description/User Story:**
As an Airline Agent,
I want to specify the quantity of each ancillary service

**Acceptance Criteria:**
1. User can select multiple ancillaries and specify the quantity for each.
2. The system validates that the quantity entered is within allowed limits. 
3. The total quantity of each ancillary is reflected in the booking summary.
4. User can update or remove the quantity of an ancillary before confirming the booking.

*System allow to specify the required quantity for a service. By default the count is 1. 
*Some services are limited to one occurence per passenger and flight
use - OncePerPassengerPerFlight : true/false to identify such items

---

##### US-Cart-13: Cart - Add selected ancillaries to cart for passengers

**Description/User Story:**
As an Airline Agent,
I want to add selected ancillaries to my booking.

**Acceptance Criteria:**
1. User should be able to view the list of available ancillaries.
2. User should be able to select one or more ancillaries.
3. User should be able to assign selected ancillaries to one or more passengers. 
4. System should calculate and display the total ancillary price before adding to cart. 
5. Upon confirmation, selected ancillaries should be added to the cart. 
6. System should display a success message after ancillaries are added to cart.
7. Error handling must be available for:
No ancillary selected
System failure
Price fetch failure
8. Ancillaries added must be visible in cart summary with passenger mapping.

EndPoint: /v2/shopping/carts/{{cartId}}/services

---

#### Feature: F1.5-SC_F2_5//Display_&_Select_Ancillary
F1.9 - SC_F2_9//Special_Assistance,_Free_Services

##### US-ViewAnc-03: ViewAnc - View the Price of Each Ancillary service

**Description/User Story:**
As an Airline Agent, 
I want to view the applicable price of each Ancillary service from the catalogue

**Acceptance Criteria:**
1. Each Ancillary should should display its corresponding price next to the service.
2. Should display correct currency and amount.
3. Any Ancillary without price should display as FREE

---

##### US-ViewAnc-04: ViewAnc - View baggage services

**Description/User Story:**
As an Airline Agent, 
I want to view a list of baggage allowance options by passenger type(PTC) and segment, with the price per baggage count.

**Acceptance Criteria:**
1. The baggage options display as a list of available baggage services in baggage section.
2. List displays the corresponding price for the number of bags and passenger type.
3. Agents can select a baggage option directly from the list for each passenger and segment.
4. The total price for selected baggage is calculated and displayed.
5. When a selection is made, the choice is stored in the booking.
6. Prices fetched from service catalogue.

---

##### US-SelectAnc-01: SelectAnc - Select Ancillaries 

**Description/User Story:**
As an Airline Agent,
I want to select one or more available ancillaries for a passenger's trip

**Acceptance Criteria:**
1. The system shall display all available ancillaries for the selected flight.
2. The user shall be able to view ancillary details such as name, description, and price.
3. The user shall be able to select one or more ancillaries.
4. The system shall update the total price dynamically based on selected ancillaries.
5. The system shall allow the user to deselect previously selected ancillaries.
6. Selected ancillaries shall be retained when proceeding to the next booking step.
7. The system shall validate availability before confirming ancillary selection.
8. Error message shall be displayed if an ancillary selection fails.
9. Screen should be responsive and aligned with UI guidelines.

---

##### US-SelectAnc-04: SelectAnc - Select Paid/Free Ancillaries

**Description/User Story:**
As an Airline Agent, 
I want to select both paid and free ancillaries from the available list.

**Acceptance Criteria:**
1. The system shall display a list of available ancillaries (both paid and free).
2. Paid ancillaries shall clearly display their price.
3. Free ancillaries shall be marked as "Free".
4. User shall be able to select one or multiple ancillaries.
5. Total price shall be updated dynamically based on selected paid ancillaries.
6. User should be able to deselect ancillaries before proceeding.
7. Selection should be saved and carried forward to the next step.

---

##### US-SelectAnc-05: SelectAnc - Proceed Without Ancillaries

**Description/User Story:**
As an Airline Agent, 
I want to confirm my order even if I do not select any optional ancillaries

**Acceptance Criteria:**
1. User should be able to proceed without selecting any ancillary.
2. System should confirm that no ancillaries are selected.
3. Order completion should be allowed without ancillary selection.
4. Order summary should exclude ancillaries if none are selected.
5. No error message should be displayed for skipping ancillaries.

---

##### US-Cart-14: Cart- View Ancillaries in Cart

**Description/User Story:**
As an Airline Agent,
I want to view the ancillaries selected in the cart

**Acceptance Criteria:**
1. The cart should display all selected ancillaries.
2. Ancillaries should be grouped per passenger per segment. 
3. User should be able to navigate back to modify ancillary selection.

---

##### US-Cart-15: Cart-View Price Breakdown of ancillaries in Cart

**Description/User Story:**
As an Airline Agent,
I want to see  the price breakdown of  ancillaries in the cart

**Acceptance Criteria:**
1. User can view price breakdown of each ancillary in the cart based on API.
 2. Breakdown includes unit price, quantity, and total amount.
 3. Total ancillary amount is calculated correctly.
 4. Price details are displayed in booking currency.
 5. Applicable taxes will shown separately.

---

##### US-Cart-16: Cart- View Grand Total for Ancillaries in Cart

**Description/User Story:**
As an Airline Agent,
I want to view the grand total of all the  ancillaries in the cart.

**Acceptance Criteria:**
1. Grand total of all selected ancillaries is displayed in the cart based on API.
2. Total updates automatically when ancillaries are added or removed. 
3. Amount is displayed in booking currency. 
4. Total applicable taxes will shown separately.
5. Total is visible before proceeding to payment.

---

##### US-Cart-17: Cart- Modify or Delete Ancillaries in Cart

**Description/User Story:**
As an airline agent,
I want the ability to modify or delete ancillaries in the passenger’s cart.

**Acceptance Criteria:**
Modify Ancillary
1. Agent should be able to change the quantity or details of an ancillary already added to the cart.
2. System should recalculate the total fare after modification.
3. Updated ancillary details should be reflected in the cart summary.
4. System should validate the availability before confirming modification.
 
Delete Ancillary
1. Agent should be able to remove an ancillary item from the cart.
2. System should ask for confirmation before deletion.
3. Total cart price should be updated after removal.
4. Removed ancillary should no longer appear in the cart summary.

*If modification or deletion cannot be performed, a clear error message should be displayed.

---

#### Feature: F1.5-SC_F2_5//Display_&_Select_Ancillary
F1.9 - SC_F2_9//Special_Assistance,_Free_Services
F1.6-SC_F2_6//Ancillary__Seatmap_(Display,_Select,_View_Price,_Add_per_Paxs,..)

##### US-ViewAnc-01: ViewAnc -View Ancillaries grouped by category and pricing type 

**Description/User Story:**
As an Airline Agent,
I want the system to display ancillary services grouped by category and separated into FREE and CHARGEABLE sections

**Acceptance Criteria:**
1. System displays all the available services grouped by category (Eg.  BAGGAGE, MEAL, LOUNGE etc)
2. System shall display the available services based on pricing category (FREE & CHARGEABLE)

---

##### US-ViewAnc-02: ViewAnc - View the Ancillary/services part of the offer

**Description/User Story:**
As an Airline Agent, 
I want the system to display the list of services that part of the selected offer

**Acceptance Criteria:**
The system shall display the list of applicable ancillaries that are part of the selected offer.

---

#### Feature: F1.6-SC_F2_6//Ancillary__Seatmap_(Display,_Select,_View_Price,_Add_per_Paxs,..)

##### US-Seat-01: Seat- Retrieve Seatmap for the offer

**Description/User Story:**
As an Airline Agent,
I want the system to retrieve the seatmap of each segment of the selected flights

**Acceptance Criteria:**
1. System should retrieve the seatmap per segment for the flights included in the offer
2. If the offer includes flights operated by other airlines the system should show a vaild information message 
3. The system should handle any other error while retrieving seatmap

*Disclaimer: Error meesage will be covered in test scenarios.

---

##### US-Seat-02: Seat - View seat service under Services Category

**Description/User Story:**
As an airline agent, 
I want to include seat service under the services category.

**Acceptance Criteria:**
1. Seat service should appear under the Services category.
2. System should display available seat options based on flight and cabin class.
3. Seat service should be selectable and added to the order.
4.Seat availability and pricing should be fetched from the existing seat inventory.

---

##### US-Seat-03: Seat- View Seat Map with Seat Types and Prices

**Description/User Story:**
As an Airline Agent,
I want to view a flight segment's seat map to see available, occupied, blocked, and paid seats with their types and prices

**Acceptance Criteria:**
1. System should display the seat layout for that segment with all available, occupied, and special seats.
2. Seats should be color coded or marked as Available , Unavailable, Special (extra legroom , exit row etc)
3. System should display only the seat map corresponding to that segment.
4. Detail information should appear on Hover eg seat number, type, price if applicable and attributes like Window , Aisle)
5. Seat Charcterstics should be shown as we are getting from API.
6. The price should be shown for Paid seats and Free indicated for non chargeable seats.
7. Seat avaialblity should be real time.
8. If seat map is not available proper error message should be shown as "Seat selection is not available on this flight. 
9. Exit row seat will not be available for non ADT passenger i.e: CHD

---

##### US-Seat-04: Seat - View Seat Map for Multi-Segment Itinerary

**Description/User Story:**
As an Airline Agent,
I want to view the seat map for all passengers across all segments in a multi-segment itinerary.

**Acceptance Criteria:**
1. Seat map should display for each segment in the itinerary.
2. All passengers in the booking should be visible on the seat map.
3. Seat status should be indicated (e.g., available, occupied, blocked, chargeable).
4. Agent should be able to switch between segments easily.
5. System must show current seat assignments, if any.
6. Seat map should display aircraft layout per segment.

---

##### US-Seat-05: Seat - Assign  Seats to the Passenger Across Segments

**Description/User Story:**
As an Airline Agent,
I want to assign seats to passengers across all flight segments.

**Acceptance Criteria:**
1. System allows assigning seats per passenger for each segment.
2. Assigned seats are correctly displayed in the cart and order summary per segment.
3. If no seat is selected on a segment, it is reflected as unassigned and display a notification when agent moved to next step.
4. Any pre-selected seat services are correctly linked to the respective segment.
5. Seat avaialblity should be real time.
6. If seat map is not available proper error message should be shown.

*Disclaimer: Error meesage will be covered in test scenarios.

---

##### US-Seat-06: Seat - Proceed with Order Without Seat Selection 

**Description/User Story:**
As an airline agent, 
I want to confirm a booking without selecting seats for passengers

**Acceptance Criteria:**
1. Agent should be able to complete the order without requiring seat selection.
2. Seat selection should be optional and can be bypass during the Order creation.
3. Order should be successfully created without seat selection.
4. Order Summary should indicate that "Seat is not Assigned"

---

##### US-Seat-07: Seat-View Assigned Seats in Cart

**Description/User Story:**
As an airline Agent, 
I want to view the seats assigned to each passenger in the cart.

**Acceptance Criteria:**
1. The cart should display seat numbers assigned to each passenger.
2. Seat information should be shown alongside the respective passenger’s name.
3. If no seat is assigned, the cart should show "No seat selected".
4. The seat details should update in real-time if the seat is changed or removed.
5. Seat information should be visible in both view and edit modes of the cart.

---

##### US-Seat-08: Seat- Modify or Delete Seats from Cart

**Description/User Story:**
As an Airline Agent, 
I want the ability to modify or delete a selected seat from the passenger’s cart.

**Acceptance Criteria:**
1. Agent should be able to view all selected seats in the cart.
2. Agent should be able to change the selected seat to another available seat.
3. System should update the fare/taxes automatically (if applicable) after seat modification.
4. Agent should be able to remove a seat selection from the cart.
5. After deletion, system should reflect updated cart value and seat status should be released back to inventory.
6. System should display confirmation messages for both modify and delete actions.

---

#### Feature: F1.7 - SC_F2_7//Fair Breakdown

##### US-Offer-15: Offers - Breakdown of Fare Components

**Description/User Story:**
I want the system to display a detailed breakdown of each fare component in the flight offer per PTC

**Acceptance Criteria:**
The system shall display price breakdown details for each flight Offer.
Break down includes:
Base Fare, Taxes, Fees, Surcharges ,...

All amounts should be shown in the currency used for pricing. 

Note: Fare Components & Prices vary per PTC

---

##### US-Offer-16: Offers - Tax Breakdown

**Description/User Story:**
I want the system to show a breakdown of the fare, taxes, VAT, GST and surcharges for each flight offer

**Acceptance Criteria:**
For each flight offer, the system must display a detailed breakdown showing the  the amount of taxes, and the amount of any surcharges.

Note: Taxes vary per PTC

---

##### US-Pay-01: Pay - Fare Summary

**Description/User Story:**
I want to see a final fare summary before generating a payment link

**Acceptance Criteria:**
Total Fare summary with selected currency

---

#### Feature: F1.8 - SC_F2_8//Only order creation without payment (No Payment_methods)

##### US-Pay-02: Pay - Trigger to generate Payment Link

**Description/User Story:**
I want the system to provide me with the option to generate a secure payment link for the current order.

**Acceptance Criteria:**
* The system must provide a button or function to generate a payment link. 
* Once generated, the link should be secure and unique to the specific order.

---

##### US-Pay-03: Pay - Payment link delivery method - Configurable per Airline

**Description/User Story:**
I want the system to send the payment link to the customer via email or SMS orboth or  to a different email address as configured by Airlines
- Option to get Payment link to a different email address or existing passenger contacts

---

##### US-Pay-04: Pay - Regenerate New Payment Link

**Description/User Story:**
I want the system to provide me with the option to regenerate a secure payment link for the current order.

My Previous payment link has to be invalid

**Acceptance Criteria:**
If the customer was not able to access the Payment link or exceeded maximum retrys with the payment link.
System allows regeneration only if the Order has a 'Pending Payment' or 'Failed Payment'.
Customer is notified via preferred contact delivery once the new payment link is generated

Note: Previously generate Payment Link should be invalidate any previous payment links  for the customer to prevent duplicate payments

---

##### US-Pay-05: Pay - Display Payment Time Limit

**Description/User Story:**
When a payment link is generated, I want the system to display a countdown timer indicating the time limit within which the customer must complete the payment.

**Acceptance Criteria:**
* Upon generating a payment link, a visible countdown timer should appear. 
 * The timer should clearly display the remaining time (e.g., in minutes and seconds). 
 * The payment time limit should be configurable by the airline. 
 * The system should indicate what happens if the payment is not completed within the time limit (e.g., order cancellation).

---

##### US-Pay-06: Pay - Handle Payment timeouts

**Description/User Story:**
I want the system to handle Payment timeouts or when the Payment time limit has  exceeded for the selected Order

**Acceptance Criteria:**
If the payment time limit has exceeded for an Order
Then the system has to automatically cancel/ close the created Order after payment timeout

---

##### US-Pay-07: Pay - Extend Payment Time limit

**Description/User Story:**
I want to extend the payment time limit for an unpaid Order

**Acceptance Criteria:**
Payment time limit extension is only available for the Order(s) with 'Payment Pending' or 'Unpaid' status  or the Payment time-limit shouldn't be expired
- Extension based on Airline configuration or customer can buy extra time by paying for it
- Original payment link remains valid during the extension period
- Confirmation message (email/ sms) is sent indicating the new expiration time

---

##### US-Pay-08: Pay - Modify Flight Offer/ Cart & Generate new Payment Link

**Description/User Story:**
I want an agent to be able to modify or choose a different offer and update the cart this resulting in change of prices, due to this agent should be able to generate a new payment link

**Acceptance Criteria:**
Given that the cart has been updated,
When the agent finalizs the new selection
When the new offer is added to the cart,
Then the total price should be revalidated resulting in change of Price
Then the system should generate a new payment linkg corresponding to the updated price

Note: Previously generate Payment Link should be invalid for the customer to prevent duplicate payments

---

##### US-OrderConfirm-01: Order - View (PNR) details

**Description/User Story:**
I want the system to display a comprehensive summary of the order details

**Acceptance Criteria:**
Order View must display all relevant order details, including: 
 * Flight information (origin, destination, dates, times, flight numbers). 
 * Primary Passenger & Contact details
 * Passenger details (names).   
* Total price including all applicable taxes and fees.

---

##### US-OrderConfirm-02: Order - Record Locator

**Description/User Story:**
I want the system to display Record Locator of the Order

**Acceptance Criteria:**
Record Locator/ PNR & owner code

---

##### US-OrderConfirm-03: Order - Breakdown of Fare & fees

**Description/User Story:**
I want the system to display a detailed breakdown of each fare component of the Order

**Acceptance Criteria:**
Detailed Order - Breakdown of Fare & Fees are displayed

---

##### US-OrderConfirm-04: Order - Creation details

**Description/User Story:**
I want the system to display Order Creation details

**Acceptance Criteria:**
Order Created Timestamp (Date & Time)
Agent ID, Name, Branch name,…
Channel, NDC, .com, Mobile App,…

---

##### US-OrderConfirm-05: Order - Payment status & Time-limit

**Description/User Story:**
I want the system to display Payment Status and Payment Time limit of the Order

**Acceptance Criteria:**
Possible Payment Status: Unpaid, Paid,…
Payment time limit: Date & Time - Valid or Expired

---

##### US-OrderConfirm-06: Order - Order Status

**Description/User Story:**
I want the system to display Order Status

**Acceptance Criteria:**
Possible Order Status: Confirmed, Closed, Opened,..

---

##### US-OrderConfirm-07: Order - OrderItem Status

**Description/User Story:**
I want the system to display OrderItem(s) Status of the Order

**Acceptance Criteria:**
Possible Order Status: Confirmed, Closed,..

---

#### Feature: F1.98-SC_F2_New_ARD_SCUI

##### US-ARD-01: Seamless navigation using Single Sign-On (SSO)

**Description/User Story:**
As a service center agent, 
I want to navigate from Service Center UI to ARDWeb using single sign-on.

**Acceptance Criteria:**
ARDWeb can be launched from Service Center UI
User is not prompted to re-enter credentials
Existing SCUI session is reused via SSO
Agent lands on ARDWeb  successfully.

---

##### US-ARD-02: Deep Link from SCUI to ARD Web Homepage

**Description/User Story:**
As a service center agent,
I want to open the ARD Web homepage directly from SCUI.

**Acceptance Criteria:**
Clicking the ARD Web link in SCUI Order details page to opens ARD Web in a new browser tab.
Agent is redirected to the configured ARD Web homepage

---

##### US-ARD-03: Deep Link from SCUI to ARD Web with PNR

**Description/User Story:**
As a service center agent,
I want to deep link from SCUI to ARDWeb with the PNR.

**Acceptance Criteria:**
Agent can initiate navigation to ARDWeb directly from SCUI.
Selected PNR is securely passed during redirection.
ARDWeb automatically loads the matching PNR details on landing.
Agent is not required to manually re-enter the PNR.
Proper error message is shown if the PNR fails to load.

---

##### US-ARD-04: Agent Instructions for Unavailable SCUI Features

**Description/User Story:**
As a service center agent, 
I want clear and consistent instructions in SCUI when a feature is not available

**Acceptance Criteria:**
In SCUI, The  global link is available for info block which clearly indicates when a feature is not available.
Instructions explain the alternative action (e.g., deep link, manual process, or other system)
Guidance is concise and easy for agents to understand.
Instructions are consistent across all unavailable features.
Content can be maintained or updated without code changes (configurable).

---

##### US-ARD-05:  Payment Redirection

**Description/User Story:**
As a service center agent, 
I want to proceed to payment after creating an order from order confirmation page.

**Acceptance Criteria:**
The agent can click the “TO Pay” button from order confirmation page.
From order confirmation page there should be a temporary link to redirect to ARDWeb.
The system redirects the agent to ARDWeb with PNR details for payment processing with same logged-in office Id in SCUI.
Any errors in order creation or redirection are displayed to the agent with actionable messages.

---

##### US-ARD-06: Global Navigation Link from SCUI to ARDWeb

**Description/User Story:**
As a service center agent, I want a global link in the Service Center UI (SCUI) that allows me to navigate to ARDWeb at any time.

**Acceptance Criteria:**
The global link to ARDWeb is visible and accessible from all screens in SCUI.
Clicking the link redirects the user to ARDWeb successfully.
No SCUI session data, user context, or transaction details are passed to ARDWeb.
ARDWeb opens in a fresh state independent of the SCUI session.
The navigation does not impact or terminate the active SCUI session.

---

### Source: User_Stories

#### Feature: Cart

##### US -21: Create Cart with Selected Offer

**Description/User Story:**
As an airline agent
I want to create a cart using the selected flight offer 
So that I can retain the pricing and availability for the passenger booking process

**Acceptance Criteria:**
Cart must be created using a valid selected offer ID
The Cart must capture all the offer components 
A unique cart id must be generated

---

##### US -22: Add Passenger Information to Cart

**Description/User Story:**
As an airline agent
I want to add passenger details to the cart so that their information can be associated with the selected offer for booking

**Acceptance Criteria:**
*Refer PassengerDetails in PassengerInformation Sheet for the details required
 * The system should allow adding information for the number of passengers selected in the previous flight selection step .

---

##### US -23: Add Passenger Contact Details - Phone

**Description/User Story:**
As an airline agent
I want to collect the mobile phone details of the passenger 
So that I can use phone as medium of communication

**Acceptance Criteria:**
*Minimum 1 contact number is required per order. 
*Purpose & category should be captured for each of the phone number. 
*Multiple contact addition with same purpose and category is allowed. Numbers should be different 
*When Purpose is "Notification"  Contact association is mandatory. For all other purpose contact association optional, is not specified It will be applied for all

---

##### US -24: Add Passenger Contact Details - Email

**Description/User Story:**
As an airline agent
I want to collect the Email details of the passenger 
So that I can use Email as medium of communication

**Acceptance Criteria:**
*Minimum 1 Email is required per order.
* purpose & category should be captured for each of the Email Addres. 
*Multiple email addition with same purpose and category is allowed. email address should be different
*When Purpose is "Notification" contact association is mandatoru. For all other purpose contact association is optional if not specified it will be applied for all

---

##### US -25: Add Passenger Contact Details - Address

**Description/User Story:**
As an airline agent
I want to collect the Postal Address details of the passenger 
So that I can use Postal Address as medium of communication

**Acceptance Criteria:**
*Minimum 1 Address is required per order.
* purpose & category should be captured for each of the Addres. 
*Multiple email addition with same purpose and category is allowed. 
Address should be different

---

##### US -26: Capture Frequent Flyer Program Details

**Description/User Story:**
As an airline agent 
I want to capture and enter the frequent flyer number and program for each passenger
So that the system can apply eligible benefits or personalized offers.

**Acceptance Criteria:**
Frequent Flyer Number - Company Code is Configurable per airline
Refer FFN sheet for the parameter details.

---

##### US -27: Verify the Passenger Field level Information

**Description/User Story:**
As an airline agent
I want to validate the passenger information before proceeding to next steps
So that I can ensure all information is complete and valid

**Acceptance Criteria:**
Passenger validation must check passenger info, required contact details. required document details etc.
Validation of DOB against PTC type.
Validaion of all the required fields.
Validation of passenger association against contact purpose - Notification
Validation of names based on name type 
     Universal - supporting only ASCII characters
     Native - (supporting all Unicode characters) 
     Romanized - this corresponds to the romanized version (in ASCII characters) of a      native name. Romanized nameType addition is not supported. 
A passenger can have more than 1 name.  Only one Universal name addition is allowed
isPreferred need to be declared in case if multiple names are added.

---

##### US -28: Modify Passenger Details in the Cart

**Description/User Story:**
As an airline agent
I want to modify the passenner details in the contact
So that I can correct the mistakes if any to proceed with the booking

**Acceptance Criteria:**
System should provide an option to modify the passenger information.
*Removing all passengers and Removing specific passengers are possible
*PTC is cannot be changed.

---

##### US -29: Modify Passenger Contact Details in the Cart

**Description/User Story:**
As an airline agent
I want to modify the passenner contact in the contact
So that I can correct the mistakes if any to proceed with the booking

**Acceptance Criteria:**
System should provide an option to modify the passenger contact details  
(Add New, Delete Existing Contact, Change the existing contact)
Contact Details include - Phone, Email, Address

---

##### US -30: Modify Existing Offer in Cart

**Description/User Story:**
As an airline agent
I want to replace the existing offer in the cart with new offer
So that I can respond to ccustomer changes in travel preference

**Acceptance Criteria:**
System should remove the previous offer and add the new one
Cart must be repriced after replacement

---

##### US -31: Revalidate the Cart after Modification

**Description/User Story:**
As an agent,
I want the cart to be automatically revalidated when any offer or service is modified
So that I ensure the data is current and the price is accurate

**Acceptance Criteria:**
System should check for offer validity and availability upon modification
Errors should be shown if offer is no longer available.

---

##### US -32: Retain Passenger and Contact Details on offer changes

**Description/User Story:**
As an airline agent
I want the system to retain passenger and contact details when modifying offers
So that I dont need to re-enter and complete booking quickly

**Acceptance Criteria:**
Passener data should persisit unless incompatible with new offer
Cart must preserve FFN, PTC, Contact Info, Regulatory Doc

---

##### US -33: Review Cart Summary before Order Creation

**Description/User Story:**
As an agent, 
I want to review  and validate the cart contents 
So that I can verify cart information and ensure the offer item, fare and services are still valid before order creation

**Acceptance Criteria:**
Cart review must include all the items present in the cart including the flight offer, passenger details, additional services if any etc. 
System must recheck the validity of the offer item(s) in the cart.
Expired items should be flagged with appropriate messages

---

#### Feature: Display Offers

##### US -9: View Matching Flight Details for a search input

**Description/User Story:**
As an airline agent
I want the system to display detailed flight information that matches the search input
So that I can present travel options to customer

**Acceptance Criteria:**
*The system must retrieve and display flight matching the input details
*The flight details must include the details mentioned in FlightDetails
*Seats Available for booking/Remaining seats
*If no matching flights are found, the system must include return message"No Offer found for given search criteria"

---

##### US -10: Display services and amenities entitled for each flight segment

**Description/User Story:**
As an airline agent
I want the system to display the services and amenities included for each of the flight
So that I can inform customers about what they are entitled to during their journey to make informed decisions.

**Acceptance Criteria:**
*For each of the flight option returned, the system must display amenities & services included in the fare for each flight segment. 
The services must be shown for each passenger type where ever applicable
*Only services applicable to the requested fare brand should be displayed
*Optional services should be marked separately.

---

##### US -11: Display Offer Terms & Conditions

**Description/User Story:**
As an airline agent
I want the system to display the terms and conditions associated with each offer, including refund,cancellation policies 
So that I can clearly communicate the fare rules to the customer to make informed decsions

**Acceptance Criteria:**
For each flight offer returned in the search result, the system must display applicable fare conditions
If the fare rule is different for each PTC, it should be displayed separately. 
The terms and conditions must reflect all segments and fare brands included in the offers.

---

##### US -12: Display Breakdown of Fare Components

**Description/User Story:**
As an airline agent
I want the system to display a detailed breakdown of each fare component in the flight offer
So that I can transparently communicate pricinng structure to customers

**Acceptance Criteria:**
The system shall display the following components separately 
Base Fare, Tax, Fee, Surcharge 
The breakdown must be shown for each flight segment
All amounts should be shown in the currency used for pricing.

---

##### US -13: Display Fare Details Per Passenger Type

**Description/User Story:**
As an airline agent 
I want the system to display fare details categorized by passenger types
So that I can understand and explain fare differences among passenger groups

**Acceptance Criteria:**
The system must show fare breakdown separately for each passenger type
For each PTC, system should list 
No. of passengger of that type
Base Fare,Tax,Fee,Surcharge 
Totals must be calculated and displayed per PTC.

---

##### US -14: Display Total Fare for All Passengers

**Description/User Story:**
As an airline agent
I want the system to calculate and display the total payable fare for all passengers
So that I can give the customer a final amount without manual calculations

**Acceptance Criteria:**
The system shall compute and display
   Total base fare for all passengers
   Total taxes
   Total Fees
   Total Surcharges
A grand total should be displayed prominently
The currency should match the fare calculation currency
The display should clearly distinguish between subtotal and grand total

---

##### US -15: Sort Flight Offers - Best Match

**Description/User Story:**
As an Airline Agent, I want the system to sort flight offers by the airline's definition of best match so that I can quickly present the most relevant options to the customer.

**Acceptance Criteria:**
* The system must sort flight offers based on a pre-configured "Best Match" algorithm determined by the airline.
Use "ranking" field in Amadeus response.

---

##### US -16: Sort Flight Offers - Departure

**Description/User Story:**
As an Airline Agent, I want the system to sort flight offers by departure time so that I can easily find the preferred flights for the customer.

**Acceptance Criteria:**
* The system must allow sorting of flight offers based on the departure time for each bound. (Both Ascending and Descending)

---

##### US -17: Sort Flight Offers - Arrival

**Description/User Story:**
As an Airline Agent, I want the system to sort flight offers by arrival time so that I can quickly identify flights based on preferred arrival time

**Acceptance Criteria:**
* The system must allow sorting of flight offers based on the arrival time for each bound. (Both Ascending and Descending)

---

##### US -18: Sort Flight Offers - Total Price

**Description/User Story:**
As an Airline Agent, I want the system to sort flight offers by total price so that I can immediately show customers the most economical options.

**Acceptance Criteria:**
* The system must allow sorting of flight offers based on the total price for all passengers in the search request. The total price should include fare, taxes, and surcharges. 
*Sorting based on low to high and high to low should be possible

---

#### Feature: Payment

##### US-34: Initiate Payment For Validated Cart

**Description/User Story:**
As an agent 
I want to initiate the payment process after the cart is validated
So that the system can create a pending order and trigger payment steps for traveler

**Acceptance Criteria:**
*Agent can trigger payment once cart validation is successful
*System must create a temporary order ID internally
*System must trigge a payment initiation notification to the AY payment gateway
*The notificaiton should include the order id, traveller contact details, country from where traveller is calling, traveller preferred language and agent remarks 
* When notification is triggered agent will see the order id with payment status as pending
Travller may proceed to payment

---

##### US-35: Display order status post payment trigger

**Description/User Story:**
As an agent 
I want to retrieve and monitor the order status after payment is initiated
So that I can confirm whether the payment is successful or not.

**Acceptance Criteria:**
Agent can retrieve the order using the order ID and see the payment status. 
system must reflect the payment status
If failed, the failure details also should be reflected in the order
Failed orders must be cancelled after a specified time period.

---

#### Feature: Search

##### US -1: Support Airline specific origin and destination lists

**Description/User Story:**
As an airline agent, 
I want the system to validate that both origin and destination are part of airline  supported locations individually 
So that only valid airports are used in search.

**Acceptance Criteria:**
Both origin and destination must be present in two separate airline-defined list
The list is based on airline configuration. The origin and destination details are accessed during search input. 
System displays only valid origin & destination airport details while typing/selecting origin
The system does not restrict based on O&D pairings,any valid origin can be searched against valid destination. 
*The Origin and Destination should not be same.

---

##### US -2: Search Offers for different Passenger tyes 

**Description/User Story:**
As an airline agent, 
I want the system to search flight offers for different passenger types (Adult,Child, Infants)
So that I can return accurate and complete pricing for the entire travel group.

**Acceptance Criteria:**
The system should accept input for each passenger type based on IATA format - ADT,CHD,INF
The total number of passengers count should not exceed 9
Age definition configurable per Airline
Adult passengers - who are 12 years of age or above at the time of the flight 
Child passengers - who are 2 years of age or above but less than 12 years of age at the time of the flight 
Infant Pax - 0 to 2 years of age at the time of flight
The search request should contain the passenger type and count

---

##### US -3: Validation of PTC count and combination in the search request

**Description/User Story:**
As an airline agent,
I want the system to validate the passenger count and PTC combination 
So that the search request is as per the recommended business standard

**Acceptance Criteria:**
Sum of ADT+CHD should not exceed 9.
Count of INF <= Count of ADT
At least 1 ADT passenger is required in the request
Sum of ADT+INF can go upto 18 (9 ADT, 9 INF)

---

##### US -4:  Flight Search - Onward

**Description/User Story:**
As an airline agent
I want to perform a fixed date search for the onward segment of a journey
So that  I can retrieve relevant flight offers scheduled for the specific onward travel date.

**Acceptance Criteria:**
The system should accept onward travel date as a mandatory input for the search

System should validate presence of other required parameters - Origin,Destination, Passenger type and count. 

Validate the required parameter details and return error if invalid.

System should return all flight offers available for the specified onward date

If no flights available, system shall return a meaningful message 

Optional filter like preferred fare brand or cabin also should be accepted

---

##### US -5: Fixed Date Flight Search - Return

**Description/User Story:**
As an airline agent,
I want the system to allow me to perform a search for round trip journey for specific date
So that I can retrieve available round trip flight offers for that exact travel date

**Acceptance Criteria:**
The system should accept onward travel and return travel date as a mandatory input for the search

System should validate presence of other required parameters - Origin,Destination, Passenger type and count. 

Validate the required parameter details and return error if invalid.

System should return all flight offers available for the specified onward date

If no flights available, system shall return a meaningful message

---

##### US -6: Capture Frequest Flyer Number for Passengers Before Search

**Description/User Story:**
As a airline agent,
I want to capture frequent flyer nmber for each passenger before initiating search
So that the system can retrieve personalized offers for eligible travelers

**Acceptance Criteria:**
The system allows an optional entry of frequent flyer for each passennger 
The system support one FF Number per passenger 
Validate FF Number format as per airline configuration. 
If not given standard offers are fetched

---

##### US -7: Search using PTC discount code

**Description/User Story:**
As an airline agent
I want to include a passenger type discount code during flight search
So that the system returns offers applicable to that PTC discount

**Acceptance Criteria:**
System provides an optional field to enter the discount code against PTC. 
System checks for validity and compatibility of discount code against PTC. 
Return error when the entered discount code is not compatible (Eg. CHD (Child) with MIL (MIL) discount code 
Return the discounted fares against the codes.

---

##### US -8: Select Commerical Fare Family in Flight Search

**Description/User Story:**
As an airline agent
I want to include a specific Commercial Fare Family (CFF) in the search criteria 
So that I can only retrieve flight offers matching the fare family

**Acceptance Criteria:**
*System must allow selectionn of fare family codes in the search request
*Agent can select upto 3 CFFs per request. 
*CFF Application Logic will depend on Point of Commencement of the journey
*If no fare family selected return all applicable offers by default

---

#### Feature: Select Offer

##### US -19: Select an Offer from Search Results

**Description/User Story:**
As an airline agent
I want to the ability to selet a flight offer from the list of search results
So that I cann proceedd with booking the chosen option of the traveler

**Acceptance Criteria:**
Agent must be able to select only one offer at a time
Upon selectionn the system should transition to move to cart

---

##### US -20: Retain the selected offer post selection

**Description/User Story:**
As an airline agent
I want the system to retain the selected offer after I choose it
So that I can continue booking without offer expiring

**Acceptance Criteria:**
The selected offer must be retained for a defined period
Retained offer must not be change in fare or availability
Retained offer should be linked to the cart.

---

