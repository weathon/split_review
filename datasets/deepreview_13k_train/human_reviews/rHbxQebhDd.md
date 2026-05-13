# Uncertainty Aware Column Generation for Crew Pairing Optimization Using Survival Analysis

- Decision: Reject
- Scores: 5, 5, 6, 1

## Abstract
The crew pairing problem (CPP) is central to optimal planning and scheduling of operations in the airline industry, where the objective is to assign crews to cover a flight schedule at minimal cost while adhering to various logistical, personnel, and policy constraints. Despite the implementation of optimized schedules, operations are frequently disrupted by unforeseen events. This vulnerability stems from the deterministic nature of the CPP's base formulation, which fails to account for the uncertainties inherent in real-world operations. Existing solutions either aim to safeguard against a specified level of uncertainty or focus on worst-case scenarios. To this end, we propose a reliability-centric CPP formulation amenable to solution by column-generation (CG)  SurvCG, that leverages survival analysis for dynamic quantification of uncertainty using the operation patterns in historical data. Applied to CPP, SurvCG forecasts and incorporates flight connection reliability into the optimization process. Through rigorous experiments on a large-scale first-of-its-kind real-world instance under regular and irregular operating conditions, we demonstrate that SurvCG achieves unprecedented improvements (up to 61%) over baseline in terms of total propagated delays, establishing SurvCG as the first data-driven solution for uncertainty-aware reliable scheduling.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This study propose SurvCG, a reliability-focused approach to the crew pairing problem (CPP) that incorporates survival analysis and column generation to handle real-world uncertainties. By forecasting flight connection reliability, SurvCG significantly reduces propagated delays, achieving up to 61% improvement over traditional models.

### Strengths
- Survival analysis allows SurvCG to predict and include the reliability of flight connections, offering a more realistic and robust solution for crew scheduling.
- The method used here is an existing one, but there are new regulations for the framework to deal with flight schedule delays.

### Weaknesses
 - The evaluation of the calculation time for the main problem is feasible if it is relatively small, but the scalability evaluation is insufficient. Specifically, the paper lacks a rigorous analysis of how the computational cost scales with the size of the problem instance, such as the number of flights, crew members, or time horizon. Without this, it is difficult to assess the practical applicability of the method for large-scale airline operations.
- Flights not only get delayed, but also arrive earlier than expected or get canceled. It is only optimized for a part of the process. The model's focus on delay propagation, while valuable, neglects other significant disruptions that can impact crew scheduling. This narrow focus limits the robustness of the proposed approach in real-world scenarios where early arrivals and cancellations are common occurrences.
- The performance evaluation and explanation of the survival model are insufficient, and the data set is also limited. The paper does not provide a detailed analysis of the survival model's predictive power, including its calibration and discrimination. The lack of a thorough evaluation of the model's performance, coupled with the limited dataset, raises concerns about the generalizability of the results.

### Questions
- Theoretically, Could you estimate the upper and lower limits of safety evaluation?

- Please evaluate the calculation amount for the master problem and clarify the size of the current situation. If this part is challenging to execute, the frame itself will not be able to operate.

- Please evaluate the details of the survival model and the impact of the model's performance.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents an approach for dealing with flight delays in the context of airline crew pairing optimization. In particular, it proposes to add a penalty term to flight connections that relates to the risk of missing the connection in the pricing subproblem of a column generation-based approach to solving the crew pairing problem. The penalty term is computed based on a prediction that is made by a survival analysis model that is trained on historical flight dely data.

In a set of computational experiments with one instance, first the cost structure of the solution obtained with the proposed (reliable) model is compared to a those obtained with a nominal model. Then, the results from simulations that propagate the delay are compared for both solutions under variouse levels of irregularity. It turns out that the solutions obtained with the reliable model show a much smaller total progagated delay, in particular under heavily irregular conditions.

### Strengths
To the best of my knowlegde, the idea of using survival analyis for estimating missed crew connections in the context of airline crew scheduling is new and original.

Also, the idea of incorporating the risk of missing a connection via a penalty term in the pairing generation subproblem is meaningful, but at the same time often used in practice and in more sophisticated ways in the literature (e.g. in Schaefer et. al. 2005, Transportation Science).

### Weaknesses
The authors do not describe their crew pairing problem very well. The crew pairing problem is a very characterized by both a very complex set of regulations (e.g. rules related to total block time per day, total work time per day, rest requirements between duties) and rules and by a very complex cost structure, both of which are at least in parts very airline-specific. The authors neither describe which rules and regulations they consider. Regarding the cost of a pairing, it appears that the costs of a pairing additively depends on the time of the flights and on the (weighted) connection times. This is a relatively simplistic assumption since in the real world, the cost structure of a pairing is much more complex, see e.g. the paper (Atnunes et al. 2019) that was cited in the manuscript, where the cost relates to the maximum of three different values, including the guaranteed crew pay per duty.

The authors write that they use a column-generation-based solver to solve a set covering formulation of the CPP. Column generation, however, can only be used to solve the LP relaxation of this formulation. In order to solve the problem to optimality (as claimed in the paper), they need use a so-called branch-and-price algorithm which involves a lot of design decisions, and also the use of commercial LP and/or MIP solvers. This aspect, however, is not even mentioned in the paper. Also, in the experimental results section, this is not discussed, which means that the results are not reproducible at all. The paper does not even mention how long it takes to solve the problem. 

The authors vaguely write that the subproblem they solve is a shortest path problem. Without further details, one would assume that we deal with a standard shortest path problem that is easy to solve. In realistic crew pairing settings, however, the subproblem is an NP-hard resource-constrained shortest path problem. Again, this aspect should be clarified.

It is not described in detail how the value r_ij enters the optimization process. While Fig. 1 would let us assume that the prediction model is only queried when needed, that does not make too much sense to me since it should be possible to compute all r_ij values for connections in advance.

The paper seems to completely ignore the fact that the minimum connection time for crews between two flights depends on the question whether the crew remains on the same aircraft or not. Usually, if the crew stays on the same aircraft, there is no minimum connection time at all. In particular, if a flight is delayed and the crew stays on the same aircraft, there is no risk of missing the connection (which is why airlines tend to disencourage aircraft changes of crews during a duty). This aspect should be definitely be discussed in the paper, since neglecting this aspect renders the whole analysis much less useful.

The paper only focuses on flight delays, and when solving the column generation subproblem, delay propagation is not considered at all. In addition, the paper neglects complex interactions between delays and crew regulations (e.g. a large total delay may render a duty invalid) and costs (which may involve so-called time away from base). For an example how a data-driven approach to crew pairing can account for these aspects, see e.g. the Transportation Science paper (Schaefer et. al. 2005)  "Airline Crew Scheduling Under Uncertainty".

Regarding the experiments, all results are given for a single instance, and even that instance is not described very well. Only from the text I can try to infer that it deals with 243 flights, which, for real-world crew pairing is a  small-to-medium-sized problem. As mentioned above, other important aspects such as the cost structure of a pairing are not discussed.

I find that the choice of alpha=2 for the "nominal problem" is somewhat arbitrary since choosing alpha>1 means that short (and thus non-robust) connections are favored. In practice, most airlines will use some way of penalizing high-risk connections, either relying on simple rules (that are certainly more complex that just a simple factor of the connection time), or on some data-driven quantitative model. If would have been interesting to see how the survival-based approach compares to a more standard ML approach for determining delay risk.

### Questions
Please provide a description of the rule set and cost structure you used in your approach. Is my assessment right that you only use time-based costs for valuating a pairing?

 Is the pricing problem a (pure) shortest path problem, or a resource-constrained shortest path problem?  What is the algorithm you use for solving the pricing subproblem?

Please provide a more detailed description of the solution approach you use. How does the branch and price work?
In the experimental results, please tell us more about the hardware you run the experiments on, the solvers you use (if any), and regarding the solution time required; also if applicable the optimality gaps.

Is there any reason to query the delay model during the solution of the CG subproblem instead of computing all r_ij values a priori?

How does your model account for (or could be extended to account for) different connection time requirements based on whether the crew changes aircraft?

Please provide a more detailed description of the instance: How many flights does it involve? Do you consider only a single crew base? 

I encourage you to run experiments with more instances to strengthen the evaluation of your approach.

In the appendix, you perform a sensitivity analysis regarding the total cost depending on alpha. For me, it would be very interesting to see how the total propagated delay in the simulation looks like for nominal solutions computed with different values of alpha.

Also, I would like to encourage you to test your approach against additional baselines, in particular to other approaches for choosing penality costs for risky connections.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents SurvCG, a novel approach to the Crew Pairing Problem (CPP) in airline operations that integrates survival analysis into a column generation framework to account for uncertainties in flight operations. Traditional CPP formulations are deterministic and often fail to consider real-world disruptions like delays and crew absenteeism. SurvCG addresses this by predicting flight connection reliability using survival analysis models and incorporating these reliability estimates into the cost function of the CPP. The method is evaluated on a large-scale, real-world dataset from Endeavor Air's 2019 operations under various scenarios, including regular and irregular operating conditions with varying levels of delay severity. Experimental results demonstrate that SurvCG can significantly reduce total propagated delays—by up to 61% compared to baseline methods.

### Strengths
- The proposed method effectively combines survival analysis for predicting flight connection reliability with the column generation method. This integration allows the optimization process to account for uncertainties in a data-driven manner.
- Experimental results show that SurvCG can reduce total propagated delays by up to 61% compared to nominal solutions, particularly under irregular operating conditions with high delay severities (e.g., the 75R scenario) highlighting the practical effectiveness of the proposed approach.
- The authors use a comprehensive real-world dataset consisting of 97,294 flights from Endeavor Air's 2019 operations. They conduct extensive simulations across various scenarios by varying the percentage of irregular operations and delay severities. The evaluation is thorough and grounded in real operational settings.

### Weaknesses
 - While the paper references existing stochastic and robust optimization approaches for CPP, it does not seem to provide direct experimental comparisons with these methods. Without such a comparison, it is challenging to assess how SurvCG's performance stacks up against state-of-the-art robust optimization techniques under similar conditions. Specifically, the lack of comparison against methods that explicitly model uncertainty in crew pairing, such as those using chance-constrained programming or robust optimization with uncertainty sets, makes it difficult to gauge the relative advantages of the proposed survival analysis approach.
- The effectiveness of SurvCG heavily relies on the accuracy of the survival analysis model used for predicting flight connection reliability. The paper does not explore how errors or uncertainties in reliability predictions might impact the overall optimization results and whether the method remains robust under less accurate predictions. The sensitivity of the overall solution to variations in the survival model's parameters or to the use of different survival models is not investigated, which is crucial for practical implementation.
- The simulation of delays may not capture the full complexity of delay propagation in airline networks, such as cascading effects and interactions between flights. This simplification could affect the validity of the simulation results and the observed performance improvements. The simulation appears to assume a simplified delay model, potentially overlooking complex dependencies and feedback loops that are common in real-world airline operations. For example, the model does not seem to account for the impact of delays on crew availability and subsequent pairings.
- The paper does not report computational times or discuss the scalability of SurvCG in terms of solution time compared to the nominal approach. I think this information is crucial for practical implementation in real-world airline scheduling systems where time constraints are significant. The absence of detailed computational performance metrics, such as the time required to solve the column generation problem and the memory footprint, makes it difficult to assess the practical applicability of the proposed method in large-scale airline networks.

### Questions
In addition to the points mentioned in previous sections, some additional questions/suggestions:

- To strengthen the contribution, it would be valuable to include a direct experimental comparison of SurvCG with existing robust or stochastic CPP methods.
- Include information on the computational time and resources required by SurvCG compared to baselines. Discuss any additional overhead introduced by the proposed approach and whether this overhead is acceptable in practical settings.
- To demonstrate the generalizability of SurvCG, it would be beneficial to evaluate the method on datasets from multiple airlines, different regions, or more recent time periods. Of course, I imagine the data may not be readily available for these cases - if that’s the case feel free to ignore this suggestion.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper studies a crew scheduling problem in airline industry and proposes a column-generation based algorithm to dynamically quantify uncertainties using operational patterns in historical data.

### Strengths
The paper focuses on an NP-hard problem and considers uncertainties in crew scheduling, and aim to improve reliability for real-world problems.

### Weaknesses
1.	Crew scheduling is a classical problem in airline operations and is a well studied topic. I do not see new concepts or technical modeling/algorithmic challenges brought up by this paper. 
2.	Considering uncertainties in airline crew scheduling are not new, and using data-driven approaches for scheduling are not new either. The contribution of this study is very limited. 
3.	The paper only considers crew scheduling but assumes that flight schedules, flight assignment (to routes) and their gate assignments are given. This further limits the complexity of the problem and it is not considered as state-of-the-art in airline operations research area. 
4.	The column generation (CG) based algorithm is very standard and with another layer of “survival analysis” it does not seem to add significant changes or difficulty to use CG for crew scheduling. I do not see efforts being made to improve the scalability and computational complexity of CG, which could suffer from the combinatorial structure of the paper. 
5.	The proposed methods in this paper are weakly related to the focus of this conference. 
6.	I do not see any data-driven type of theoretical analysis although the authors state that they are the first to propose “data-driven solutions for uncertainty-aware reliable scheduling”. That is, how the data and sample sizes can affect the solution results and quality?

### Questions
1.	What are learning based methods studied in this paper? How this work is related to this conference? 
2.	How are the approaches proposed in this work compared to the state-of-the-art integer programming and stochastic programming based methods used for solving scheduling problems in Operations Research area? 
3.	What is the data-driven aspect of this approach? 
4.	What are the dynamic uncertainty quantification procedures used in the paper? All seem to be static except that the data and models are connected iteratively in a rolling-horizon way. This cannot be called “dynamic”.

### Soundness
2

### Presentation
2

### Contribution
1
