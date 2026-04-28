# Discrimination-free Insurance Pricing with Privatized Sensitive Attributes

- Decision: Reject
- Avg Score: 7.00
- Scores: 6, 8, 8, 6

## Abstract
Fairness has emerged as a critical consideration in the landscape of machine learn-ing algorithms, particularly as AI continues to transform decision-making across societal domains. To ensure that these algorithms are free from bias and do not discriminate against individuals based on sensitive attributes such as gender and race, the field of algorithmic bias has introduced various fairness concepts, along with methodologies to achieve these notions in different contexts. Despite the rapid advancement, not all sectors have embraced these fairness principles to the same extent. One specific sector that merits attention in this regard is insurance. Within the realm of insurance pricing, fairness is defined through a distinct and specialized framework. Consequently, achieving fairness according to established notions does not automatically ensure fair pricing in insurance. In particular, regulators are increasingly emphasizing transparency in pricing algorithms and imposing constraints on insurance companies on the collection and utilization of sensitive consumer attributes. These factors present additional challenges in the implementation of fairness in pricing algorithms. To address these complexities and comply with regulatory demands, we propose an efficient method for constructing fair models that are tailored to the insurance domain, using only privatized sensitive attributes. Notably, our approach ensures statistical guarantees, does not require direct access to sensitive attributes, and adapts to varying transparency requirements, addressing regulatory demands while ensuring fairness in insurance pricing.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper considers fairness insurance pricing problems. The method proposes to achieve actuarial fairness in insurance pricing. Actuarial fairness is different from conventional machine learning fairness concepts, like demographic parity and equalized odds. In insurance pricing, existing works mainly consider three methodologies in solving fairness: counterfactual approach, group fairness approach, and probabilistic approach. However, all aforementioned methods requiring direct access of sensitive information might not be available due to regulation.  This paper proposes a method that introduces the trusted third party (TTP) that deals with noiseless or noisy sensitive information, allowing discrimination-free premium without direct access to sensitive information.

### Strengths
This paper addresses a significant real-world challenge: achieving discrimination-free insurance pricing. The proposed method is not only grounded in solid mathematical foundations but also applicable to practical applications. It has been thoroughly evaluated through comprehensive experiments on scenarios with both known and unknown noise rates.

### Weaknesses
Please see the questions.

### Questions
1. question regarding the problem setting: Does the insurer have access to sensitive attributes, but only in an indirect manner, such that they cannot directly access these sensitive attributes? If so, the TTP may need to generate a fair premium without directly knowing the sensitive attributes. In that case, why do we still need the TTP? Could the insurer implement the method directly to generate the premium on their side instead?

2.  Why does integral over $d$ with measure $\mathbb{P}^*(d)$ bring discrimination-free price if $X$ contains information of $d$. 

3. Could the author elaborate on Theorem 4.5? What does $\tilde{\epsilon}$ represent here? When compareTheorem 4.5 to Theorem 4.3, the only difference is this term. Does it represent the error from estimating the error rate $\pi$ and $\bar{pi}$?

4. Does this condition $M_g+\frac{C_1+\theta}{ln2}>\tilde{\epsilon}>\theta$ have some meaning or is it simply a technical assumption?
.

### Soundness
4

### Presentation
3

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
This work studies the problem of providing discrimination-free insurance prices when information about true sensitive attributes is hidden from the insurer---in particular, it is held by a trusted third-party which, for example, may add noise to ensure that sensitive attributes are differentially-private. In addition to showing risk bounds for both known and unknown noise rates, the authors conduct thorough experimental evaluations for how properties of the problem instance and hyperparameters used in the algorithm affect overall performance.

### Strengths
* Exposition in section 4 is straightforward (especially leading up to Theorem 4.3). 
* Experimental evaluation is thorough and well motivated.

### Weaknesses
 * I'm not sure how realistic/practical this problem setup is at a high level; do such protocols currently exist?
* Risk bounds in section 4 seem to follow pretty 'classic' concentration-type arguments, esp. in the dependence on VC(F). This is fine, though it does mean the interpretation should be more qualitative (scaling wrt $n$ and noise level) than quantitative

Presentation comments:
* it could be helpful to have a diagram illustrating the protocol for interaction between insurer and TTP.  
* Maybe worth noting that because risk is defined wrt an arbitrary (possible per-group, if I understand correctly?) $L$, minimizing risk of $f$ is sufficient to optimize for (e.g.) the ideal price $h^*$ or whatever downstream utility the insurer gets.
* Why is the transformation $T(X)$ necessary?

### Questions
* Why is the transformation $T(X)$ necessary?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses fairness in insurance pricing where the use of sensitive attributes like race and gender is restricted. Recent regulatory demands requires approaches that prevent discrimination without directly using sensitive data. The authors propose a multi-party framework where insurers collaborate with a trusted third party (TTP) and the sensitive attributes influence pricing only indirectly.

The main contributions of the paper are: (i) The authors introduce a framework that enables insurers to calculate fair premiums without direct access to sensitive attributes, while the TTP uses a noised version of sensitive features to generate "discrimination-free" insurance prices. (ii) The authors provide theoretical guarantees for two settings -- when the noise of the sensitive features is known and unknown to the TTP. (iii) The paper demonstrates the method’s effectiveness in two insurance datasets, showing its robustness to noise and the impact of noise estimation errors on performance.

### Strengths
To start, I think this paper is a very strong paper. It studies an important research question -- fairness in insurance pricing, which is a domain that typically emphasizes actuarial fairness over algorithmic fairness. The authors introduce an innovative framework that adapts to regulatory requirements by using privatized, noised sensitive attributes for TTP to calculate discrimination-free premiums. This application of differential privacy within a multi-party setup in the insurance sector is novel and distinguishes this work from other fairness research. 

What I like about the paper the most is its high quality in its technical rigor and thoroughness. The authors offer theoretical guarantees for scenarios with known and unknown noise rates, with clear delineation of assumptions and the rigorous derivation of theoretical results. 

The paper is also well-organized and easy to follow. Key concepts, such as "discrimination-free pricing," are defined early on, and the technical sections are structured nicely, which allows readers to follow the framework’s development from problem formulation to implementation. The explanations of complex privacy mechanisms, including local differential privacy and its implications for sensitive data handling, are accessible even for readers less familiar with privacy-preserving machine learning.

The paper also provides an in-depth empirical analysis section that effectively demonstrates the method’s applicability and limitations, contributing to the clarity of the results.

### Weaknesses
1) The paper's setting relies on the feasibility of the framework via data sharing with TTP. What if this framework is not feasible, e.g., using a TTP is not feasible? Would the authors be able to comment on something along this line and also comment on the flexibility of their proposed framework under different regulatory requirements?

2) The tightness of the upper bound provided in the two theorems. 

3) It would be nice to add comparisons to existing fairness methods or baseline models for insurance pricing. 

4) The study focuses on the US Health Insurance and Auto Insurance datasets, but additional datasets -- particularly those representing other insurance types or more complex demographic distributions -- could add value.  

5) The paper could benefit from a more explicit discussion of its limitations and future directions.

### Questions
1) Could the authors provide more insights into the tightness of the upper bound presented in Theorems 4.3 and 4.5? For example, how does the gap between the empirical risk R^LDP (f)  and  R(f^*)  behave as noise decreases?

2) Do the authors see potential for this framework to be applied in domains beyond insurance? For instance, could it be adapted for fields with similar regulatory constraints on fairness and sensitive data, such as finance or healthcare?

3) The framework currently focuses on discrete sensitive attributes. Could the authors elaborate on how it might extend to continuous sensitive attributes, or discuss challenges that may arise? 

4) Could the authors explicitly discuss known limitations of the proposed approach?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper develops a method for learning a "discrimination-free" insurance pricing policy when sensitive attributes are private, and only noisy forms of these attributes are available to a trusted third party. Theoretical results are presented for the case where the privatization approach is a) fully known, b) has unknown noise rates. The method is applied to health and auto insurance datasets.

### Strengths
Though I'm not an expert in privacy-preserving ML, this paper's theoretical results are probably of interest to people in that field.

After revisions, this paper sufficiently discusses the practical implications of the proposed approach to insurance markets and customers in those markets.

### Weaknesses
UPDATE: After discussion and revisions, I believe the paper has adequate answers to these questions. Though I'd like to see the substantive impacts of the proposed approach get even more attention in the paper, I think the authors have done enough to merit acceptance.

The experiments and evaluation section in this paper claims to show that the method "achieves fair pricing effectively", but it answers none of the questions that would allow us to determine if such pricing is fair, effective, or desirable. 

* How much do men and women pay for insurance after this method is applied?
* How does this compare to the benefit they receive from insurance payouts?
* Which other subgroups benefit or are made worse off by this method?
* If insurance is under/overpriced it could lead to adverse selection, where, for example, high-risk male drivers buy more insurance because it’s cheap, increasing premiums for everyone else. It could even lead to people driving more dangerously at the margin because they know that an incident won’t increase their premiums much. Is there risk of adverse selection or other negative equilibrium effects from using this pricing?

This paper paper is clearly trying to develop a method for pricing that can be used by real insurers. Unfortunately, though, it treats insurance pricing as an exercise in privacy math, and not as an input to a crucially important product for people's physical and financial health.

Convergence in a linear model with 6 features requiring thousands of epochs seems very slow to me - what's causing this?

What's the reason for prioritizing convergence rate in the experiments? This doesn't seem like an important property of insurance pricing algorithms (unless, of course, the model diverges), since the time and expense of training the model will likely be very small compared to the revenue and expenses of actually delivering insurance.

### Questions
Please see my questions on the important practical implications of this method above. In addition:

Convergence in a linear model with 6 features requiring thousands of epochs seems very slow to me - what's causing this?

What's the reason for prioritizing convergence rate in the experiments? This doesn't seem like an important property of insurance pricing algorithms (unless, of course, the model diverges), since the time and expense of training the model will likely be very small compared to the revenue and expenses of actually delivering insurance.

### Soundness
3

### Presentation
3

### Contribution
3
