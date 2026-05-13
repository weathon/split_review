# LLM Unlearning via Loss Adjustment with Only Forget Data

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Unlearning in Large Language Models (LLMs) is essential for ensuring ethical and responsible AI use, especially in addressing privacy leak, bias, safety, and evolving regulations. Existing approaches to LLM unlearning often rely on retain data or a reference LLM, yet they struggle to adequately balance unlearning performance with overall model utility. This challenge arises because leveraging explicit retain data or implicit knowledge of retain data from a reference LLM to fine-tune the model tends to blur the boundaries between the forgotten and retain data, as different queries often elicit similar responses. In this work, we propose eliminating the need to retain data or the reference LLM for response calibration in LLM unlearning. Recognizing that directly applying gradient ascent on the forget data often leads to optimization instability and poor performance, our method guides the LLM on what not to respond to, and importantly, how to respond, based on the forget data. Hence, we introduce \textbf{F}orget data only \textbf{L}oss \textbf{A}justmen\textbf{T} (\textbf{FLAT}), a "flat" loss adjustment approach which addresses these issues by maximizing $f$-divergence between the available template answer and the forget answer only w.r.t. the forget data.
The variational form of the defined $f$-divergence theoretically provides a way of loss adjustment by assigning different importance weights for the learning w.r.t. template responses and the forgetting of responses subject to unlearning.
Empirical results demonstrate that our approach not only achieves superior unlearning performance compared to existing methods but also minimizes the impact on the model’s retained capabilities, ensuring high utility across diverse tasks, including copyrighted content unlearning on Harry Potter dataset and MUSE Benchmark, and entity unlearning on the TOFU dataset.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces FLAT (Forget data only Loss Adjustment), a novel method for unlearning in large language models (LLMs) without requiring retain data or a reference model. By leveraging f-divergence maximization between template and forget responses, FLAT achieves unlearning solely based on the forget data. The empirical results across three datasets show that the method offers competitive performance, effectively balancing forget quality with model utility.

### Strengths
The proposed FLAT method addresses a critical limitation in existing LLM unlearning techniques by eliminating the need for retain data or reference models, making it highly practical for real-world applications where such data is often unavailable. The paper provides a thorough theoretical foundation for the method, supported by the use of f-divergence as a guiding principle for loss adjustment. Furthermore, the extensive experiments on diverse datasets (Harry Potter, TOFU, and MUSE benchmarks) demonstrate the versatility and robustness of the method. The paper also situates FLAT well within the landscape of existing methods, clearly delineating its advantages.

### Weaknesses
While FLAT demonstrates strong performance, its advantages over simpler baselines, such as the Mismatch method, appear marginal in some scenarios. For instance, in Table 3, the FLAT (KL) method outperforms alternatives but only slightly, raising questions about the practical significance of these improvements. Additionally, the performance of Mismatch is not consistently included in all subsequent experiments (e.g., Tables 6 and 7), which could provide a clearer comparative analysis.

The paper also lacks an ablation study on Step 1 (template response generation), despite its pivotal role in the method. Variations in template design could significantly impact unlearning performance, and exploring these effects would enhance the methodological insights.

### Questions
1. Step 1 (template generation) seems to offer various alternatives and variations. Have the authors conducted ablation studies to evaluate the impact of different template response strategies on unlearning performance?
2. Can the authors provide additional analysis on why simpler baselines, such as Mismatch, occasionally achieve comparable results and how FLAT specifically addresses these edge cases?

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
3

### Summary
This paper introduces FLAT, a method for LLM unlearning that does not require access to retain data to maintain model utility. The idea of FLAT is to obtain a model that maximizes the f-divergence between an example response distribution (how the model should respond on the forget data) and the forget response distribution (distribution of forget data). Experiments on three LLM unlearning datasets demonstrate that FLAT can balance the forget effectiveness and model utility, without access to retain data.

### Strengths
1. This paper studies an important question of how to perform LLM unlearning when retain data is not available. The paper provides a new perspective from f-divergence, which is missing in existing LLM unlearning works and could benefit future research.
2. The paper conducts experiments on three datasets, covering different popular LLM unlearning settings.

### Weaknesses
1. My main concern is about the performance of the proposed method. Particularly, on TOFU, FLAT does not show a significant improvement compared to baselines. Most methods achieve similar forget quality (FQ) and model utility (MU), so it's unclear if the improvement is significant or not. Additionally, why is the reported FQ much lower than the NPO paper? On 1% subset, the NPO paper reports a FQ greater than 0.8. The retain performance in Tables 3 and 5 also does not show a significant improvement.
2. Several related works that also perform unlearning without retain data are missing [1-3]. Particularly, the name change algorithm in [1-2] is not compared. In [2], it shows that this method achieves a much higher FQ while maintaining the MU, without access to retain data.
3. The presentation of the paper, especially the methodology section, is confusing. Specifically, it is stated that the goal is to maximize the f-divergence in Eq 3. However, how exactly does $\theta$ appear in Eq 3? Based on the description of the algorithm, both distributions $\mathcal{D}_e$ and $\mathcal{D}_f$ seem to have nothing to do with $\theta$. $\mathcal{D}_f$ is the distribution for the forget data, and $\mathcal{D}_e$ is the distribution for the example response on the forget data. So what does it mean to maximize Eq 3 with $\theta$? How is Eq 4 derived from Eq 3? Some notations, such as $h$, are also confusing. It appears in multiple equations, but it seems sometimes it's the predicted probability for a specific token, and sometimes it's just a predicted token.

### Questions
Please see the weaknesses. Additionally,
1. Why is the TOFU experiment only conducted on 1% subset? Most works evaluate on all 1%, 5%, and 10%, and it seems 10% is a more difficult setting.
2. What does it mean to satisfy a criterion in Table 5?
3. Why is VerbMem calculated using only 1 prefix token? It does not make much sense to only have a single-token prefix.
4. Why does Table 6 report different metrics from other experiments on TOFU?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper explores a method for LLM unlearning with only the data designated for forgetting, rather than relying on both forget and retain data. The proposed method employs a weighted loss function comprising two terms: one term encourages the model to produce template/refusal response for the forget data, and the other term discourages the model from generating the original. The experimental results suggest that this method achieves a favorable trade-off between forgetting accuracy and retaining the model's overall performance.

### Strengths
* The paper studies a relaxed unlearning setting for LLMs that does not require retain data, which may be challenging to obtain in some cases. 
* The experiment involves multiple benchmarks, diverse LLMs, and various baseline unlearning methods to offer a comprehensive assessment of the proposed approach.

### Weaknesses
 * Unclear Motivation for f-divergence Reweighting: I did not quite follow the method section. Specifically, I think using f-divergence to reweight the loss terms with coefficients $\lambda_e$ and $\lambda_f$ remains unclear. The method section (specifically lines 197-215, step 3) states that this maximizes the f-divergence between $D_e$ and $D_f$. But I'm not fully clear why this is beneficial for LLM unlearning. The connection between maximizing f-divergence and the desired unlearning outcome is not explicitly established. It's unclear how this reweighting mechanism ensures that the model effectively forgets the specific information while retaining other knowledge. The paper does not provide a clear explanation of how the f-divergence maximization translates to improved unlearning performance compared to simpler weighting strategies.
* Limited Performance improvement: The experimental results do not clearly demonstrate a significant advantage of the proposed method over baseline methods. For example, the forget quality on the TOFU dataset is similar to that of the baseline methods. Additionally, the NPO method paper reports a substantially higher forget quality (close to 1.0) in the TOFU-1% unlearning scenario, yet Table 4 reports a much lower forget quality for NPO (6e-3). This discrepancy raises concerns about the reliability of the reported results and the effectiveness of the proposed method. The lack of a clear performance advantage over existing methods, especially on the TOFU dataset, weakens the overall impact of the paper.
* Scalability Concerns: The experiments focus only on the TOFU-1% unlearning setting for TOFU dataset, which involves forgetting information on only 2 authors out of 200 in the synthetic dataset. There is no result on the performance of the method with larger forget sets, such as the TOFU-5% or TOFU-10% settings, raising concerns about the scalability and generalizability of the proposed method. The absence of results on larger forget sets makes it difficult to assess the method's robustness and its applicability to more realistic unlearning scenarios.

### Questions
* How is the alternative answer sampled? Is it generated by the model undergoing unlearning, or by a separate LLM?
* It seems that the primary difference between the proposed objective function and the SimPO objective function is the weight for the two loss terms. Is there an intuitive explanation for why the proposed f-divergence-based weighting would perform better than the approach used in SimPO?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes FLAT, an LLM unlearning method that only requires "forget data" for parameter update. FLAT is driven by an optimization loss that maximizes the f-divergence between the forget data and the forget query paired with expected unlearned responses. The authors finds in this way model can implicitly choose a balance between promoting exemplary and suppressing bad generations of forget data. Experimental results show FLAT's superiority against previous baselines. More importantly, FLAT does not require optimizing models on "retain data" or any reference model to achieve unlearning.

### Strengths
1. FLAT is a method without using "retain data" or reference models, which is novel and potentially more efficient against previous baselines.
2. Paper is easy to follow. Proof is provided.
3. Experiments are comprehensive and convincing.
4. I like the informative appendices.

### Weaknesses
1. Not really a lot of weaknesses. I just feel that some experimental settings should be more clearly discussed. Please refer to the questions below.
2. Some repeated contents in the main body and I suspect some equation is not correct. But I can understand. Please refer to the questions.

### Questions
1. Should line 235 be log prob inthe equation? Since you have a sum rather than multiplication on probabilities.
2. Line 371. PO should have the lowest PPL as shown in Table 3.
3. On TOFU dataset. Did you first finetune base LLMs on fictitious data (including forget, reatin and held-out) and then perform unlearning? I think you should add one sentence explaining that. And the forget quality measures the how close the unlearned model’s output matches a model trained only on the retain data. Should here the input into the unlearned model the input of forget data? Then why we should expect the unlearned model resembles a model trained only on the retain data? I feel very confused with this setting. Could you provide clearer explanation?
4. I am also wondering why on Harry Potter you used Forget Quality Gap, which is the difference in ROGUE L and and BLEU. However in TOFU you choose to directly compare the ROGUE-L between unlearned model and retained model. As pointed our in line 408, low ROGUE-L doesn’t necessarily indicate to better performance. Then why you still use Forget Quality Gap in Harry Potter?
5. Is line 512-515 repeated content?

### Soundness
4

### Presentation
3

### Contribution
4
