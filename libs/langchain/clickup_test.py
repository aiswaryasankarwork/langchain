import os

from langchain.agents.agent_toolkits.clickup.toolkit import ClickupToolkit

from langchain.agents import AgentType, initialize_agent
from langchain.llms import OpenAI
from langchain.utilities.clickup import ClickupAPIWrapper
import requests

oauth_client_id = "VR9ER2KI35L9SL4QWQD3VXK5UUUQBCD9"
ouath_client_secret = "O5E2F09WQG4BVDF283ZYLWBWT4OPJPNL0KDKKU08U3EJ3MH00FXVF1II9UOCS5KG"
code = "S695H3CSYBXDDZU8JKO6M79QNQES7N6G"

clickup = ClickupAPIWrapper(oauth_client_id=oauth_client_id, oauth_client_secret=ouath_client_secret, code=code)

toolkit = ClickupToolkit.from_clickup_api_wrapper(clickup)
llm = OpenAI(temperature=0, openai_api_key="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")

agent = initialize_agent(
    toolkit.get_tools(), llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

# Tasks available 
tasks = [
    "https://staging.clickup.com/t/333/CLK-337140", 
    "https://staging.clickup.com/t/333/RDMP-7690",
    "https://staging.clickup.com/t/333/CLK-337723",
    "https://staging.clickup.com/t/333/CLK-338765",
    "https://staging.clickup.com/t/333/RDMP-7376",
]

questions = {
    "RDMP-7690": [
        "What discussions or decisions regarding the product features are mentioned in the conversation, and how do they affect the development timeline?",
        "Are there any unresolved concerns or issues that need further discussion?",
        "Can you provide insights into how the MVP (Minimum Viable Product) for the timesheet feature has evolved over time?",
        "What criteria were used to prioritize and de-prioritize features and improvements within the project?",
        "What are the key user requirements and value propositions for the timesheet and approval feature?",
        "How have these requirements changed, and which ones are considered essential for the MVP?",
        "How has the availability of resources, including developers, impacted the development timeline and feature prioritization?",
        "Are there specific challenges or roadblocks that have affected the project's progress?",
        "What considerations have been given to permissions and roles within the timesheet and approval system?",
        "Can you describe the proposed role of managers in approving timesheets and any related functionalities?",
        "In the context of approvals, what level of granularity is expected for entries, such as day-level vs. week-level approvals?",
        "How will comments and approvals be handled, and what actions can managers take?",
        "Has a competitive analysis been conducted to understand how similar features are implemented in competing products?",
        "What were the findings from this analysis, and how are they influencing feature design?",
        "How is the implementation of timesheets and approvals linked to different product tiers, such as business, plus, and enterprise?",
        "Are there opportunities for feature segmentation based on different user needs?",
        "How do the ongoing developments in timesheets and approvals align with client expectations, and have there been any changes?",
        "Can you provide information on any presentations or demonstrations that clients might find useful in understanding the project's status?",
        "What is the current status of development and the anticipated timeline for the project, considering resource allocation and priorities?"
    ],
    "CLK-337140": [
        "What are the concerns related to the high number of calls to /data/guide.json, and how does this affect the system's performance?",
        "Is there an existing configuration to control or reduce the frequency of Pendo guide calls, and if so, where can it be found?",
        "How did the team attempt to mitigate the issue using the 'preferMutationObserver,' and what were the results of this approach?",
        "Are there insights into the internal workings of Pendo, and how might it be possible to change or delay the interval for DOM checks?",
        "Can you explain the recommendation to define requirements for enabling or disabling Pendo, and what are the potential impacts of this approach?",
        "What conditions should be met for Pendo to be enabled or disabled, and how can it be toggled for local testing?",
        "Are there specific Pendo features that can be disabled and re-enabled as needed, and what's the purpose of these toggles?",
        "How do developers ensure that Pendo is working locally when pointed to a staging environment, and what might be missing in this setup?",
        "Can you provide more information about the window.pendo flag and its impact on the system's behavior?",
        "How does the current issue with Pendo calls impact application performance and user experience?",
        "Is there a plan to analyze the number of Pendo calls made during specific user actions, such as loading list views and viewing tasks?",
        "How does the proposed change in the 'ignoreHashRouting' setting affect Pendo's behavior, and what is its relation to route changes?",
        "Can you explain the reasons behind the decision to mark this issue as 'Not-A-Blocker,' and what are the implications for the production release?",
        "How does the Pendo change impact the system's startup, list view loading, task view loading, and board view loading times?",
        "What other potential solutions have been considered to reduce the number of Pendo calls and their impact on the system?"
    ],
    "CLK-337723": [
        "What is the primary goal related to the comments, and what does the team aim to achieve in terms of reducing calls?",
        "How did the team determine if a user is online or offline, and what were the challenges with the previous methods?",
        "Is leveraging the WS ping-pong to determine online status a viable solution, and what potential issues are associated with it?",
        "What's the suggestion regarding delaying the call to the favicon on successful XHR calls, and how does this affect user experience?",
        "What is the idea of using HTTP_INTERCEPTORS to monitor network calls, and have there been any challenges with this approach?",
        "Why is the size of the favicon important, and what alternative file type has been suggested for this purpose?",
        "How has the team ensured reliability and performance while dealing with network calls and user online status?"
    ],
    "CLK-338765": [
        "How did the team determine the issue mentioned in Comment ID 98020014817134, and what context is provided to understand it?",
        "What is the approach being suggested to monitor the frequency of calls to the page API, and why is this important?",
        "What's the current volume of calls to the mentioned endpoint, and how does it impact the system?",
        "Has the team identified any experienced individuals, like @Sergiy, @Konstantin, @Alex Yurkowski, who could provide insights into solving this issue?",
        "How can users reproduce the issue described in Comment ID 98020014825843, and what section of the application is responsible for the network request multiplication?",
        "What progress has been made in the tasks associated with the epic? Has the issue of over-fetching mentions been resolved?",
        "Is the team still facing issues with the high volume of requests to v1/task endpoints, and what measures have been taken to address them?",
        "Have there been any identified causes for the regression causing the spike in requests, and has it been fixed?",
        "What are the updates regarding the mentioned Slack conversation and the resolution of issues related to task mentions?",
        "Is the issue flagged as a blocker, and what steps are being taken to address it?",
        "How has the team addressed and resolved the issue of over-fetching mentions, and which areas were specifically impacted?",
        "What future monitoring and investigations are planned to ensure better performance in areas like task description, doc content, doc history, and inbox?"
    ],
    "RDMP-7376":  [
        "What are the considerations for showing the description as HTML without initializing the full quill editor?",
        "What implications are associated with implementing the change discussed?",
        "What are the main reasons for concerns related to this change?",
        "What differences exist when rendering a Delta with deltaToHtml?",
        "How can cursors and live updates be enabled when rendering in HTML?",
        "What potential user experience issues may arise when clicking into the description?",
        "What is the estimated time required for creating a quill instance and rendering content?",
        "Have any profiles or videos been saved for comparison and analysis?",
        "Is there a focus on task view V3 or V2 when addressing the task?",
        "Is there a plan to re-evaluate Docs render scheduling?",
        "What are the possible scheduling strategies for rendering Docs?",
        "What is the status of the task related to slow task description loading?",
        "What additional changes are being considered as part of this task?",
        "Who is responsible for the QA review of the task, and who should assist if it touches list view?",
        "Is there a request for assistance from a task squad QA member?",
        "Is there a need to test different sizes of tasks for validation?",
        "Are there sample tasks available for testing?",
        "What is the purpose of reviewing a video, and what approval is being sought?",
        "What does the spinning loading indicator represent in the video?",
        "What should be tested regarding the description loading and app usability?",
        "Is there a plan to merge the changes to QA?",
        "What is the purpose of merging the task for cutoff?",
    ]
}

num_success, num_failure = 0, 0
for ticket, questionList in questions.items():
    for question in questionList:
        try:
            print(question)
            agent.run("In ticket " + str(ticket) + ", " + question)
            num_success+=1
        except Exception as e:
            print("Failed to answer question with error: " + str(e))
            num_failure+=1

print("The agent solved " + str(num_success) + " questions correctly and failed to answer  " + str(num_failure))



