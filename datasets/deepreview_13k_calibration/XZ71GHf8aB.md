# Evidence from the Synthetic Laboratory: Language Models as Auction Participants

- Decision: Reject
- Avg Score: 6.25
- Scores: 8, 6, 6, 5

## Abstract
This paper investigates the behavior of simulated AI agents (large language mod-
els, or LLMs) in auctions, validating a novel synthetic data-generating process
to help discipline the study and design of auctions. We begin by benchmarking
these LLM agents against established experimental results that study agreement or
departure between realized economic behavior and predictions from theory; i.e.,
revenue equivalence between first-price and second-price auctions and improved
play in obviously strategy-proof auctions. We find that when LLM-based agents
diverge from the predictions of theory, they do so in a way that agrees with behav-
ioral traits observed in the existing experimental economics literature (e.g., risk
aversion, and weak play in ‘complicated’ auctions). Our results also suggest that
LLMs are bad at playing auctions ‘out of the box’ but can improve their play when
given the opportunity to learn. This learning is robust to various prompt specifi-
cations and holds across a variety of settings. We run 2,000+ auctions for less
than $250 with GPT-4o and GPT-4, and develop a framework flexible enough to
run auction experiments with any LLM model and a wide range of auction design
specifications.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This manuscript asks, "how well do LLMs substitute for humans in auctions"? - a question motivated by the cost of experimenting with human subjects: the c. 1,000 auctions run for the manuscript cost less than US\\$100 on GPT-4 and GPT-4o - in contrast to the US\\$15,000 price of the human experiments (with 404 subjects) in Li (2017).

The paper first describes the LLM simulation environment (§2).  Then §3 forms the bulk of the paper, introducing the auction designs (first and second price sealed bid - FPSB and SPSB - as well as the strategically equivalent ascending auction, AC, and a 'blind' variant, AC-B, which does not report when bidders drop out).  For each, theoretical and (human) experimental results are presented.  These are compared to the LLM results.

The findings are:
1. consistent with theory, LLMs bid higher in the SPSB than in the FPSB, although with a "smaller separation ... than would be predicted by theory" - largely due to overbidding relative to theory in the FPSB;
1. in AC - which is 'simpler' than the strategically equivalent auction SPSB - LLM play is closer to theoretically predicted play.  This is found in both independent private values (IPV) and affiliated private values (APV) settings.

### Strengths
**originality**

The manuscript is original in the sense of being the first I have seen to assess LLMs as human substitutes in auctions.

**quality**

The research is well reasoned, conducted and written up.

**clarity**

The manuscript is generally clear.

**significance**

To use the expression of Dell'Acqua et al. (2024), the capabilities of LLMs form a 'jagged frontier' relative to human performance, requiring task-by-task analyses.  This manuscript contributes to that endeavour.

### Weaknesses
1. above all, I wonder what problems are solved by the discovery that LLMs in stylized environments play roughly like humans do.  Thinking aloud, some guesses:
   1. testing failure modes in advance of high-profile auctions.  Even given the relatively low costs of LLM use, this seems an inefficient way of proceeding relative to e.g. randomly generating bid data or formally proving properties (q.v. Caminati, Kerber, Lange and Rowat, 2015).  To be convinced, I would want to see how well LLMs perform in more asymmetric auctions, e.g. calibrated to real high-profile auctions, or perhaps the Combinatorial Auction Test Suite (Leyton-Brown, 2024). Specifically, the current setup with a small number of bidders and simple value distributions may not reveal the limitations of LLMs in more complex scenarios. The paper would benefit from exploring settings with heterogeneous bidders, correlated values, or more intricate auction rules to better assess the practical utility of LLMs in this context.
   1. assistance in gaining intuitions in theoretical analysis of novel auction formats (q.v. Dütting, Feng, Narasimhan, Parkes, and Ravindranath, 2024).  Here, the manuscript would be more convincing if it showed us insights into novel auction formats - instead of just the most common ones. The focus on standard auctions limits the potential for LLMs to provide new theoretical insights. A more compelling demonstration would involve using LLMs to explore less well-understood auction mechanisms, potentially uncovering novel bidding behaviors or equilibrium properties.
2. It is claimed (p.2) that LLMs may exhibit risk-aversion even when prompted not to.  The evidence for this claim is in Appendix A.4, which is not part of the submission.  Thus, I am unable to assess this claim.  I would, in particular, like to see it compared to other hypotheses. Without access to the appendix, the claim of risk aversion is unsubstantiated. It is crucial to provide evidence supporting this claim and to compare it against alternative explanations for observed bidding behavior, such as bounded rationality or strategic uncertainty.
3. It is claimed (p.3) that Li (2017) found "that human subjects tend to be more truthful in second price sealed bid auctions than in ascending clock auctions".  Again, I would want to see which other hypotheses were considered by Li: one can imagine sunk cost arguments affecting ascending clock bids, but not SPSB.  (A similar comment arises on p.8, when it is claimed that humans "are less truthful" under AC-B: alternatively, might they not just have more difficulty with the Bayesian calculation?) The paper should delve deeper into the potential reasons for the observed differences in human behavior, beyond simply stating that humans are more or less truthful. Alternative explanations, such as cognitive biases or the complexity of the auction format, should be considered.
4. It would be nice to see performance considered for varying $n$.  The manuscript indicates that $n$ is "often" three (p.3) or always three (p.4), which - I would guess - may account for around half of the examples in an LLM's training data.  Thus, it is possible that performance deviates from human considerably outside of the training data. The reliance on a fixed number of bidders raises concerns about the generalizability of the findings. Exploring the impact of varying the number of bidders would provide a more robust assessment of LLM performance and its sensitivity to changes in the auction environment.
5. Other interesting robustness tests could include:
   1. compare results for auctions identical up to the 'currency' units (e.g. dollars, billions of cowrie shells, etc.). 
   1.  compare results with and without the first step of the simulation procedure (p.3), which asks the LLM to generate a bidding plan explicitly: which result is closer to amateur/expert human bidding? The paper should explore how sensitive the results are to the specific framing of the auction and the simulation procedure. Examining the impact of different currency units and the explicit bidding plan generation step would provide valuable insights into the robustness of the findings.
6. I would probably cite Vickrey's original paper for the results on his eponymous auction, rather than Krishna's 2009 textbook (p.5).
7. The panels in Figure 1 are reversed: that on the left, for which the bid = value in theory, is the SPSB, not the FPSB.
8. Given the importance of Li's OSP (2017), I would like a bit more space given to its explanation (e.g. maybe removing the table at the bottom of p.4, if needed).

### Questions
1. footnote 5 mentions setting a non-zero temperature to induce variation.  _Prima facie_, this might seem to correspond to something other than a BNE - like a trembling hand, or QRE?  (If so, than the comparison to BNE theoretical results is inappropriate.)
1. valuations in the FPSB and SPSB are drawn uniformly, but bids are constrained to be integers (p.4).  In general, equation (2), the FPSB BNE bid, does not resolve to an integer.  Is there any reason to believe that whatever rounding strategy is used does not introduce artefacts into the results?
1. there is evidence that, with training, humans learn to play close to Nash (pp.5, 8).  While the abstract claims that LLMs "can improve their play when given the opportunity to learn", the text (p.8) finds, "little evidence of learning over time".  Which of these is correct?  Either way, it may be useful to be more careful to compare like-for-like humans and LLMs (e.g. amateur/untrained v experienced/trained).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies how well LLMs can simulate human behavior in auctions. The key motivation behind this work is that generating synthetic data using LLMs could potentially offer a cheaper alternative to traditional human-subject experiments.    

The findings show that LLMs sometimes deviate from the predictions of economic theory, but these deviations often align with the behavioral traits observed in real-world experiments with human participants. In particular, the LLMs tend to underbid in second price auctions and overbid in first price auctions, yielding a counter argument to revenue equivalence. This can be explained by risk aversion in LLM bidding behavior. Additionally, the paper reveals that LLMs perform better in simpler auction formats (clock auctions), which supports the argument behind the obvious strategy-proofness.    

The authors suggest that LLMs could be a valuable tool for studying a wide range of economic mechanisms, including those that are currently difficult or impossible to test experimentally.  They highlight the potential of LLMs to generate data for large-scale experiments that would be too costly or raise ethical concerns if conducted with human participants.

### Strengths
This paper moves along an exciting application of LLMs in experimental economics, and could be a valuable and unique plus to ICLR. The economic properties being examined in this paper are fundamental and the observations from LLMs are interesting.

### Weaknesses
One major challenge to this line of research (LLMs as an alternative to human-subjects in experiments) is that the behavior of the LLMs could be highly sensitive to (1) training data and (2) prompt, which may put the reliability of observations from experiments with less known results at risk. More importantly, the complete prompts used in this work are not shared and there seems no robustness test of the LLM behavior against the prompts.

Taking the first prompt template in Appendix A.1 as an example, where “RULE EXPLANATION”, “INSTRUCTIONS”, “PERSONA” are not given. I used this template by only filling the rule explanation part and observed very different results (i.e., the bidding plan from the LLM).
* If I describe the auction rule of second price auction in a less formal way (in the tongue of ordinary people), the LLM replies things like slightly overbidding and randomized bidding etc.
* If I describe the auction rule of second price auction in a formal way (in the tongue of an auction theorist, e.g., using “sealed bid second price auction”), the LLM immediately says “my dominant strategy is to bid my true valuation of the item”.

From the simple test above, we can see that response from the LLM could depend on (1) whether they learned how to play this game from training data (they may know the literature of the experiment already) and (2) whether the prompt properly recalls the corresponding memory.

Therefore, a crucial component of studies like this would be a robustness test.

### Questions
What are the prompts used as “RULE EXPLANATION”, “INSTRUCTIONS”, “PERSONA” in this work?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the auction behavior of simulated AI agents (LLMs) and validates a synthetic data-generating process for auctions.
Precisely, this paper benchmarked LLM agents against established experimental results in auctions, such as revenue equivalence between first-price and second-price auctions and behavior in obviously strategy-proof auctions. It is found that when LLMs diverge from theory, their behavior aligns with some human behavioral traits observed in experimental economics literature (e.g., risk aversion). Also it is shown that LLMs can improve their play with learning opportunities and this learning is robust across settings.

### Strengths
1. Provides insights into how LLMs perform in auction scenarios, which is relevant as LLMs are increasingly being considered for various economic applications.
2. Conducts a detailed analysis of LLMs' behavior in different auction formats and settings, including semantic analysis and counterfactual experiments to understand their decision-making processes.

### Weaknesses
1. "Each setting is repeated 15 times with values drawn randomly each time." It is hard to say whether 15 samples are enough to represent a random distribution. The concern is that with only 15 repetitions, the observed behavior of the LLM agents might be highly sensitive to the specific random draws of values, potentially leading to results that are not generalizable or representative of the underlying distribution of agent behaviors. This is especially critical when analyzing the nuances of auction behavior, where even small variations in valuations can lead to different strategic choices. A larger sample size would provide more robust statistical power to detect meaningful patterns and reduce the risk of spurious findings.
2. It is a pity there is no theoretical result can be derived or developed based on the experiments. While the empirical findings are interesting, the lack of a theoretical framework to explain or predict the observed behaviors limits the broader impact of the work. The paper could benefit from an attempt to formalize the observed deviations from standard auction theory into a model that could be further analyzed and tested. Without such a theoretical grounding, it is difficult to assess the generalizability of the findings beyond the specific experimental setup.

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the auction behavior of LLMs. They benchmark LLM agents against two kinds of existing experimental results. The first result is that realized human biddings differ from theoretical results in first-price and second-price auctions. The second result is that clock auctions induce more rational play in humans than second-price auctions. The authors systematically designed prompts and their results show that the behavior of LLMs conforms with the aforementioned experimental results.

### Strengths
1. The study of LLMs in auctions are interesting and relatively new.

2. In the appendix, the authors include robustness checks, which make the results more convincing.

3. The main structure of the paper is clear. Each benchmark begins with the setting, proceeds to existing theoretical and empirical results, and ends with simulation outcomes, which make it easy to be understood.

### Weaknesses
1. My main concern is that the technique contribution of this paper is limited. The method and design of experiments are simple and not novel.

2. The results claimed in abstract are not clearly presented.
  * The authors claim that 
>Our results also suggest that LLMs are bad at playing auctions ‘out of the box’ but can improve their play when given the opportunity to learn.
>
   On one hand, it not clear which part of their results shows that LLMs are bad at playing auctions ‘out of the box’. On the other hand, in sec 3.2.4, they mention that 
>Interestingly, we see little evidence of learning over time.
>
This seems to contradict with the conclusion in the abstract and I think clarification is needed.

* The authors claim that 
>..., validating a novel synthetic data-generating process to help discipline the study and design of auctions.
>
And the authors actually ask two research questions:
>The present work examines this question for auctions: how well do LLMs substitute for humans in auctions, especially when behavioral traits like risk-aversion or bounded rationality matter? And, more generally: how can we use LLMs to improve the design of economic mechanisms?
>
The first question is answered well. But it is not clear that which part of their results discusses using this process to improve the design of economic mechanisms.

Overall, I suggest the authors summarize their research questions and contributions in a more explicit way.

### Questions
1. Why the authors use LOESS-smoothed data for regression? Is it standard? I think a few explanations are needed here.

2. In sec 3.2.4, the auctions repeat 15 rounds and the LLM agents seem not improve their understanding of the mechanisms by bidding closer to their true value over time. Did the author try to repeat the auction more than 15 rounds?

### Soundness
2

### Presentation
3

### Contribution
2
