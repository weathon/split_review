## Human Reviewer 1

### Questions
-please address the concerns I raised in the weakness section of this review in above, i.e., comparative evaluation relative to existing multi-agent approaches, guarantee of correctness (e.g., feasibility of the the plan resulting from meta-planner that generated dependency graphs and constraint models), robustness to changing events, etc…

- can authors comments on instances that the framework will be limited to handle and will produce errors and failures? What mechanisms is in place to handle such cases?

-can authors also comment on the cost and benefit analysis of the proposed multi-agent approach planning vs a single agent planning framework together with some form of feasibility check. Can authors comments on large scale problem solving capabilities? What about optimality? For example, how the performance behave as the number of cities increases in the TSP problem. Do authors expect trade offs would be necessary.

Other questions:
-There is no info about which side of suburb grandma is living, so LLm cannot know if there is better route for Michael. Your criticism of suboptimality of the solution given by DeepSeek appears invalid.

-The assignment in equ 5 is not ensuring that the agent will satisfy the constraint. Just like the thanksgiving dinner example, these agents are all qualified to meet the constraint but they simply did not in the single LLm case. This will happen in the proposed system too. LLM can even ignore your instructions because of its overfitting bias.

-a diagram of the overall system would be very helpful. It is strange that the authors preferred to verbally describe everything without any illustration of how the components are interrelated.

### Rating
2

### Confidence
5

---

## Human Reviewer 2

### Questions
No

### Rating
1

### Confidence
3

---

## Human Reviewer 3

### Questions
Could the authors elaborate on how MACI quantitatively and qualitatively compares with existing multi-agent frameworks (e.g., Multi-LLM Debate, CAMEL) in terms of performance and adaptability in dynamic planning scenarios?

### Rating
2

### Confidence
4