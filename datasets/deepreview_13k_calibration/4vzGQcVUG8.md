# Provable weak-to-strong generalization via benign overfitting

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
The classic teacher-student model in machine learning posits that a strong teacher supervises a weak student to improve the student's capabilities.
    We instead consider the inverted situation, where a weak teacher supervises a strong student with imperfect pseudolabels. 
    This paradigm was recently brought forth by \citet{burns2023weak} and termed \emph{weak-to-strong generalization}. 
    We theoretically investigate weak-to-strong generalization for binary and multilabel classification in a stylized overparameterized spiked covariance model with Gaussian covariates where the weak teacher's pseudolabels are asymptotically like random guessing.
    Under these assumptions, we provably identify two asymptotic phases of the strong student's generalization after weak supervision: (1) successful generalization and (2) random guessing. 
    Our techniques should eventually extend to weak-to-strong multiclass classification. 
    Towards doing so, we prove a tight lower tail inequality for the maximum of correlated Gaussians, which may be of independent interest.
    Understanding the multilabel setting reinforces the value of using logits for weak supervision when they are available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper investigates weak-to-strong generalization in the setting of an overparameterized spiked covariance model with Gaussian covariates. The paper identifies an asymptotic phase transition between successful and unsuccessful generalization.

### Strengths
The math appears correct to me; the problem is significant, and desiderata 1 and desiderata 2 make sense.

### Weaknesses
The paper is rather technical, and the clarity could be improved significantly to make it more readable. (see questions)

1. The main setup is quite confusing to me. The paper first states that "$f_{weak} \in \mathbb{R}^d$" is the object we learn. Normally, the model is a function, not a vector, so this was not immediately clear. It is defined later in line 347 how we learn $ f $, which is quite far from where it was introduced (line 184). It would be better to define that we train $f$ by MNI earlier. Specifically, the paper should clarify the relationship between the vector  $f_{weak}$ and the function it represents. Providing a more explicit definition of how $f$ is parameterized and trained using the minimum norm interpolation (MNI) method would greatly improve the understandability of the initial setup.

2. In line 201, it says, "As a consequence of our main results in Section 3, we will show that the above desiderata are achievable in a simple toy model; see Theorem 3.3 for a formal statement." However, Theorem 3.3 only considers desiderata 1.2 and 2.1, not the entirety of the desiderata. The paper should explicitly address how the other desiderata (1.1, 1.3, 2.2) are handled within the framework of Theorem 3.3 or provide pointers to other sections or theorems where these desiderata are addressed. This will ensure a comprehensive understanding of how the proposed model satisfies all the stated desiderata.

3. What is "$t$" in Equation (3) of Theorem 3.1? The paper needs to define $t$ immediately after introducing it in the equation. It is stated that $k = n^t$, but the connection between $t$ and the number of label classes in the multiclass problem is not obvious. Providing a clear definition and its relation to the problem setup would enhance the clarity of the theorem.

4. The notation $ u, p, q, r $ used is not very intuitive, and it makes the result difficult to interpret. Is there a simpler way to rephrase the result? Specifically, the paper could provide a table or a section where these variables are defined and their significance explained in the context of the spiked covariance model. Additionally, exploring alternative representations or providing intuitive explanations for these variables' roles in the key equations could significantly improve the interpretability of the results. For example, relating these variables to more common statistical or machine learning concepts might make the results more accessible to a broader audience.

### Questions
1. The main setup is quite confusing to me. The paper first states that "$f_{weak} \in \mathbb{R}^d$" is the object we learn. Normally, the model is a function, not a vector, so this was not immediately clear. It is defined later in line 347 how we learn $ f $, which is quite far from where it was introduced (line 184). It would be better to define that we train $f$ by MNI earlier.

2. In line 201, it says, "As a consequence of our main results in Section 3, we will show that the above desiderata are achievable in a simple toy model; see Theorem 3.3 for a formal statement." However, Theorem 3.3 only considers desiderata 1.2 and 2.1, not the entirety of the desiderata.

3. What is "$t$" in Equation (3) of Theorem 3.1?

4. The notation $ u, p, q, r $ used is not very intuitive, and it makes the result difficult to interpret. Is there a simpler way to rephrase the result?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The papers identifies a specific setting under which weak to strong generalization occurs. Consider a strong model that learns a classifier on strong features of the data by supervised learning on $m$ weak labels given by a weak model that was trained on weak features on $n$ clean labels. Then weak to strong generalization implies that 

Condition 1):  The strong model has perfect classification accuracy whereas the weak model has close to random accuracy. 

Condition 2): The generalization is due to weak labels, i.e. if the strong model was only trained on $n$ clean labels, there is no generalization.
 
The setting is as follows: A learner observes features distributed according to a Gaussian distribution, $x \sim N(0, \Lambda)$ where $\Lambda$ is diagonal covariance matrix following a bilevel ensemble parameterization 
\begin{equation}\lambda_j = \lambda_F =  \frac{ad}{s} \text{ for } 1 \leq j \leq s \text{ otherwise } \lambda_j = \lambda_U = \frac{(1-a)d}{d-s}\end{equation}
where $d = n^p, s= n^r, a = n^{-q}$ and $p > 1; q, r >0; q+ r < p$. For multiclass setting, classes are further scaled as $k = c_k n^t$ for some $t<r$.  The strong model observes features given by some $p, q, r$ and weak model observes features  characterized through $p_{weak}, q_{weak}, r_{weak}$. In particular the strong features $x_{strong}$ and weak features $x_{weak}$ are given as 
$$ x_{strong} = N(0, \lambda_F I_{[s]} + \Lambda_U I_{[d]/[s]}) $$
$$ x_{weak} = N(0, \lambda_{F, weak} \Pi_S + \Lambda_{U, weak} \Pi_T)$$
for some subsets $S \subseteq [s], T \subseteq [d]/[s]$ and $\Pi_S$ denotes projection onto axis aligned subspace indexed by $S$. $\lambda_{F, weak}  = \frac{a_{weak}d_{weak}}{s_{weak}}$ and $\Lambda_{U, weak} =  \frac{(1-a_{weak})d_{weak}}{d_{weak}-s_{weak}}$.

 The true labels are given by $y = \text{sign}(x_1)$ for binary classification and $y = \arg\max_k (x_1, \dots x_K)$ for $K$ way classification. 


 
In this parameterized setting, the authors show that there is a particular regime of number of weak labels $m$ provided by the weak model (for certain regimes of $p, q, r, p_{weak}, q_{weak}, r_{weak}$) where weak to strong generalization occurs (condition 1) holds). The conditions (for binary classification) are given by (assuming $m = n^u$)

1. $u + \min(1 -r,  p + 1 - 2(q + r)) > q_{weak}+r_{weak} > (p_{weak} + 1)/ 2$
2. $p + 1   >  (q + r + q_{weak} + r_{weak})$
3. $u < (p + 1 + q + r  - (q_{weak} + r_{weak})/ 2)$ 

Further the classification error of strong learner trained on $n$ cleaned labels is shown to be depend as 
$$1/2 - 1/\pi \arctan (\Theta(n^{p+1 - 2(q+r)}))$$

Thus they claim one can identify regimes under which condition 2) also holds (possibly when $p+1 - 2(q+r) << 1$) although no details are provided).

Further they provide an informal claim and details in appendix that there exists some regime for multi class setting.

### Strengths
Exact characterization of the regime where weak to strong generalization occurs in terms of parameters of the covariance matrix of strong and weak features.

### Weaknesses
Most of the important details are pushed into appendix. The main body only contains one useful theorem which identifies a certain condition where condition 1) of weak to strong generalization holds. Setting for condition 2) and multi class settings are merely mentioned as claims. The main body also does not provide proof sketch or provide insights into the proof of the theorem.

The lack of a detailed discussion on condition 2) is a significant weakness. The paper claims that it reduces to checking conditions from Theorem 3.1, but this is not immediately obvious and requires more justification. The multi-class setting is also treated too superficially, with only an informal claim and details relegated to the appendix. This makes it hard to assess the generality of the results. The absence of a proof sketch in the main body makes it difficult to understand the core ideas and techniques used to derive the main theorem. This lack of transparency hinders the reader's ability to grasp the significance and limitations of the result.


### Questions
Suggestions:

1. Reduce the introduction - it currently spans 2 pages. 
2. Figure 1 is useless.
3. The section on data model was not particularly needed. Page 5 and 6 can be compressed into 1 or 2 paragraphs.
4. Include some experiments in main body.

In general the paper is quite verbose, it can be compressed substantially and content moved back into main body.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
In this work, the authors provide theretical justification for the empirically observed phenomenon of weak to strong generalization. In this setting, a weak learner is used to created labelled examples (from unlabelled training data) that is used to further train a stronger model. The intuition is that the weak learner has learnt some useful information about the ground truth and hence the pseudolabels it generates will actually enable generalization. The authors prove that this weak to strong generalization has two phases: (1) when the number of pseudolabelled examples is less than some threshold, the strong learner behaves like a random guesser, (2) beyond the threshold the strong learner achieves perfect generalization. A technically interesting tool that they use is a new lower tail for the max of correlated gaussians which could be of independent interest.

### Strengths
1) This work addresses the important problem of obtaining theoretical justification for a frequently encountered empirical phenomenon
2) The lower tail for max of correlated gaussians is an interesting result.

### Weaknesses
See questions.

### Questions
21) What the the word "represent" mean in Desiredata 1.(ii).
2) What is the significance of the bi-level-ensemble? 
3) What is $t$ in Theorem 3.1?
4) Is there a reason for choosing a halfspace for the ground truth? Does this analysis extend to other concepts. Is there a similar notion for regression (rather than classification)?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper studies a toy-model for weak-to-strong generalization. They show that under the assumptions of their toy-model, two asymptotic phases occur for the student: (1) it is able to successfully generalize or (2) the student resorts to effectively random guessing. The authors also try to extend their results to weak-to-strong multiclass classification and derive new lower tail inequalities for the max of correlated gaussians.

### Strengths
- The paper studies a phenomenon that has been empirically observed and thus relevant to practice
- The results and proof techniques seem non-trivial and interesting

### Weaknesses
I find the organization and presentation a bit confusing and hard to parse. In particular, Theorem 3.3 is hard to interpret without referencing the Desiradatum outlined in Section 2. Ideally, Theorem 3.3 should be standalone and at the very least, the variables in Theorem 3.3 like $\tau_{weak}, p_{weak}, ...$ should be defined. In addition, and in my opinion, the notation and current presentation of the result doesn't really make it seem like this is a "simple, toy model", given how many free variables there are to keep track of.  One possible fix is to give more intuition and less notation about the toy-model in the main text, and push the details into the Appendix. For example, I think it would be really helpful to have an informal, non-rigorous theorem summarizing the main result in the Main Contributions section.

In addition, I am not sure what to take away from this paper. It is nice that you found a toy example, where you can provide rigorous evidence of the empirical phenomena of weak-to-strong generalization. However, I am not convinced this toy model is realistic/relevant to practice, even after reading the Modeling assumptions in the Discussion. In short, it would be nice if the authors can answer:
-  **why** one should care about finding a "simple, concrete theoretical setting where we can provably exhibit different phases of weak-to-strong generalization?"
- what can I take away from this result?

### Questions
See weaknesses above. It would be nice if the authors can address these.

### Soundness
3

### Presentation
2

### Contribution
3
