# Hot PATE: Private Aggregation of Distributions  for Diverse Tasks

- Decision: Reject
- Scores: 6, 8, 6, 6

## Abstract
The Private Aggregation of Teacher Ensembles (PATE) framework is a versatile approach to privacy-preserving machine learning. In PATE, teacher models that are not privacy-preserving are trained on distinct portions of sensitive data. Privacy-preserving knowledge transfer to a student model is then facilitated by privately aggregating teachers' predictions on new examples. 
 Employing PATE with generative auto-regressive models presents both challenges and opportunities. These models excel in open ended \emph{diverse} (aka hot) tasks with multiple valid responses. Moreover, the knowledge of models is often encapsulated in the response distribution itself and preserving this diversity is critical for fluid and effective knowledge transfer from teachers to student. In all prior designs, higher diversity resulted in lower teacher agreement and thus -- a tradeoff between diversity and privacy. Prior works with PATE thus focused on non-diverse settings or limiting diversity to improve utility.
   We propose \emph{hot PATE}, a design tailored for the diverse setting. In hot PATE, each teacher model produces a response distribution that can be highly diverse. We mathematically model the notion of \emph{preserving diversity} and propose an aggregation method, \emph{coordinated ensembles}, that preserves privacy and transfers diversity with \emph{no penalty} to privacy or efficiency. We demonstrate empirically the benefits of hot PATE for in-context learning via prompts and potential to unleash more of the capabilities of generative models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces HotPATE, a method based on the Private Aggregation of Teacher Ensemble with the distinction that the method forgoes independent teacher data and models. In fact, the teacher coordinate their sampling such that upon aggregation of their votes, rare teacher decisions (for instance, rare tokens in the case of private synthetic next-token generation) can still be produced without requiring a lot of agreement between teachers. The paper claims this process improves the diversity of the resulting vote histograms without privacy cost of not having high agreement  (which is traditionally what ensures low PATE privacy costs for private prediction). A new definition for diversity-preserving aggregeation of distributions is presented. Empirical results show that under that definition, HotPATE improves upon ColdPATE. However, practical implications of the definition and broader contribution is unclear.

### Strengths
- Improving diversity of PATE responses is an interesting goal, given how much the privacy of PATE comes from teacher agreement (therefore lack of diversity in teacher votes).
- The idea of coordinated sampling of tokens seems novel. Although its privacy implications are unclear.

### Weaknesses
As someone who is quite familiar with PATE and its derivatives, I found this paper very hard to read and digest. I think there are a couple of reasons for this:

- **A robust privacy analysis is missing.** The paper introduces a particular histogram aggregation strategy that produces rate token frequency. In a sense, this is not an aggregation that produces a single vote but rather a transformed histogram. Overall, I found the presentation of this rather simple idea overly complicated in Section 3. However, the key issue here is not the contrived procedure and Definition 1, but rather the complete lack of privacy analysis under this new aggregation method. Let me clarify this point: the PATE privacy analysis only holds under the noisy argmax release. In particualr, the analysis is a function of the gap between the top vote and the second top vote of the histogram. If we were to use Def.1 and instead release transformed vote count (for the purposes of diversity), we are strictly releasing more information. In fact, since the rare token frequencies are kept (for diversity purposes), such a scheme will likely have higher privacy cost than releasing a full noised histogram of votes.

- **Writing and exposition is not polished.** The introduction is too long and full of technical detail with frequent forward references. None of the technical terms first appearance receive proper introduction.  I find page 4 almost completely incomprehensible as a result. New terms are frequently used before they are properly defined. For instance, "homogeneous ensembles" is used in Line 186 but partially defined in Line 191. Some terms are really never properly defined at all in the introduction ("diversity", "robustness parameter", etc.)

- **Experimental results are limited.** The results are mostly validating that the algorithm produces more "diverse" tokens. I think this is necessary and good. However, throughout the paper it is unclear what the value of this "diversity" is. I was hoping the experimental results would showcases a concrete benefit from having more diverse tokens. For instance, better generalization (test error) on a down-stream task.

- **Empirical results contain no privacy quantification.** Although the paper seeks to find the trade-off between privacy and diversity, the empirical section contains no quantification of the privacy budget of the algorithm. Coupled with the fact that a proper privacy analysis is missing (see first point above) I have serious doubts regarding the privacy claims of the paper and the empirical section did not do much to alleviate them.

### Questions
- Can you ground your notion of diversity in a practical example? Why should one adopt your notion of diversity? What utility does it bring? Can you provide concrete empirical results to support the benefit of improved diversity as you define it?
- I had a lot of trouble with your presentation of the suggested method as a privacy-preserving algorithm. Having read the paper, I am not convinced of claims such as Line 337:
  > This high agreement allows rare tokens to pass even with high privacy noise and allow for the aggregate distribution, with fixed privacy requirements, to satisfy Definition 1.  
Can you make a clear case for this?  
- Have I misunderstood part of your work? To be clear, I think as is, this paper is not ready for publication. However, I want to be fair and make sure that I have not misunderstood your work. So I'll be happy to engage with you during the rebuttal process.

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces Hot PATE, an extension of the PATE (Private Aggregation of Teacher Ensembles) framework, to settings where output diversity is important. PATE works by partitioning the data and training a teacher model on each partition. Then, for a given model input, the each teacher model "votes" on a label, and a final label is privately sampled from the teacher histogram. 

The key idea of Hot PATE is to preserve both privacy in the output label and the diversity of teacher distributions. The paper introduces the property of diversity preserving aggregation and introduces ensemble coordination as a technique to satisfy the property. Ensemble coordination strategically introduces correlation between teacher votes to ensure that rare tokens are transferred with high privacy noise, effectively mitigating the privacy penalty associated with high diversity, due to private sampling.

The authors provide an empirical demonstration of this approach in the context of in-context learning and show that Hot PATE yields greater diversity in output tokens.

### Strengths
- Introduces an extension of PATE that overcomes the diversity-privacy tradeoff
- Motivates the analysis through the notion of diversity preserving aggregation
- Connects proposed method with existing statistics literature: coordinated sampling
- Paper reads well, particularly with comparisons between hot and cold PATE

### Weaknesses
 - The empirical analysis is more along the lines of a proof-of-concept rather than a thorough comparison. The paper would benefit from more systematic experiments between hot and cold PATE. Specifically, the paper lacks a detailed exploration of how the level of coordination impacts the diversity and privacy trade-off. It would be beneficial to see experiments that vary the degree of shared randomness and analyze the resulting changes in both the output diversity and the privacy guarantees. The current experiments only demonstrate the existence of the effect, but do not provide a comprehensive analysis of its behavior under different conditions.
- No discussion of the limitations of the proposed methods. The paper should discuss the computational overhead of coordinating ensembles, especially in scenarios with a large number of teachers or high-dimensional output spaces. Furthermore, the paper should address the potential for the shared randomness to introduce biases or correlations that could negatively impact the overall performance or fairness of the model. It is also important to discuss the practical challenges of implementing coordinated sampling in real-world systems, such as the need for synchronized random number generators across different teacher models.

### Questions
1. In practice, does increasing diversity ever harm utility?

Other Notes:

- Typo on Line 93: "...include component that..."

- Typo on Line 190: "...two use scenarios of applications..."

- Typo on Line 323: "A tokens j that..."

### Soundness
3

### Presentation
4

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
Private Aggregation of Teacher Ensembles (PATE) was designed for classification-like tasks where each datapoint has a single ground-truth label. For “diverse" tasks such as sequential text generation, the responses might instead be distributions. But there is a tension between diversity and privacy: diversity in the responses reduces agreement among the teachers, which in turn requires a smaller noise scale and less privacy. This paper proposes “hot PATE” which allows for higher diversity in the responses without increasing the privacy cost.

### Strengths
* I think this paper has a significant contribution — via a carefully designed aggregation method, PATE can now thrive in a broader and more modern setting. Formalizing the notion of “diversity-preserving” (Definition 1) is also a helpful contribution.
* The PATE framework can now be applied to very fashionable problems such as in-context learning.

### Weaknesses
 * The paper is not beginner-friendly and seems to assume a reader who is already very familar with DP, PATE and LLMs. In fairness, this probably is going to be the chief audience of this paper, but at the same time I find it somewhat egregious that differential privacy is never formally defined (even if the definition has to be deferred to the appendix due to space constraints).
* I felt that the privacy guarantees are not rigorously stated, DP implementations are largely left as poorly-described black boxes (e.g., NoisyArgMax in Algorithm 2 is never formally introduced) and none of the algorithms include the privacy parameters as input. I didn't see a formal privacy analysis that can be easily verified, and in terms of reproducibility I feel like the algorithms can’t really be implemented without knowing, for example, how to calibrate the noise scale.

### Questions
* Besides coverage and diversity, are there other metrics which could be used to demonstrate the effectiveness of hot PATE?
* Line 274: If I’ve understood correctly, “the noise scale must satisfy $\sigma << \arg \max_j c_j$” is a requirement on the utility, and not the privacy? It might be helpful to explain this more thoroughly.

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces "hot" PATE, an extension of PATE designed for in-context learning via prompts, addressing tasks that are "diverse" and open-ended. They empirically demonstrate the potential of hot PATE for in-context learning.

### Strengths
1. The motivation is clear: sequential text generation tasks through in-context learning are inherently diverse ("hot") with multiple valid responses.


2. The idea of aggregating responses from different teachers to maintain both diversity and privacy is interesting.

### Weaknesses
1. My primary concern is the empirical evaluation. The utility of in-context learning is typically measured by accuracy in the literature (e.g., [1,2,3]). However, this paper does not report in-context learning accuracy on specific tasks. It is unclear how much benefit hot PATE can provide for in-context learning. Additionally, the experiment is conducted on only one dataset, which is insufficient, and there is only one baseline ("cold" PATE). It is unclear why comparisons to prior in-context learning work (e.g., [1,2,3]) are not included.


2. The paper states that Wu et al. (2023), Lin et al. (2024), and Xie et al. (2024) are independent concurrent work, which is inaccurate. These should be considered prior work, as Wu et al. (2023) and Lin et al. (2024) were published at ICLR 2024, and Xie et al. (2024) at ICML 2024.


3. I suggest extending the literature review of this paper by including the work "Tang, Xinyu, et al. Privacy-Preserving In-Context Learning with Differentially Private Few-Shot Generation. The Twelfth International Conference on Learning Representations.". This work studies differentially private in-context learning and proposes to use the sample and aggregate framework to generate DP synthetic examples for in-context learning inference. It could also serve as an experimental baseline for comparison.



3. Some typos:

(1) I recommend ensuring the correct application of \citet and \citep.


(2) Missing periods in Line 299, Line 396, and Line 427.

### Questions
As in the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2
