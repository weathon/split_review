# Where have you been? A Study of Privacy Risk for Point-of-Interest Recommendation

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 5, 8, 5

## Abstract
As location-based services (LBS) have grown in popularity, more human mobility data has been collected. The collected data can be used to build machine learning (ML) models for LBS to enhance their performance and improve overall experience for users. However, the convenience comes with the risk of privacy leakage since this type of data might contain sensitive information related to user identities, such as home/work locations. Prior work focuses on protecting mobility data privacy during transmission or prior to release, lacking the privacy risk evaluation of mobility data-based ML models. To better understand and quantify the privacy leakage in mobility data-based ML models, we design a privacy attack suite containing data extraction and membership inference attacks tailored for point-of-interest (POI) recommendation models, one of the most widely used mobility data-based ML models. These attacks in our attack suite assume different adversary knowledge and aim to extract different types of sensitive information from mobility data, providing a holistic privacy risk assessment for POI recommendation models. Our experimental evaluation using two real-world mobility datasets demonstrates that current POI recommendation models are vulnerable to our attacks. We also present unique findings to understand what types of mobility data are more susceptible to privacy attacks. Finally, we evaluate defenses against these attacks and highlight future directions and challenges

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes data extraction and membership inference attacks to POI recommendations involving location data. The experiments are conducted in two datasets and the empirical results show the effectiveness of the proposed attacks.

### Strengths
1. The research problem is important.
2. The paper analyzes the factors in the data that affect the attack performance.
3. The proposed attacks for data extraction and membership inference attacks are simple yet effective.

### Weaknesses
1. The appropriate baselines are missing. Can the existing data extraction or membership inference attacks be applied to the POI recommendation models, e.g., [1]? It's not clear why the authors chose not to compare against existing membership inference attacks, especially given the claim that their method is an adaptation of existing techniques. A more thorough evaluation would include comparisons to established methods in the field to demonstrate the specific advantages of the proposed approach.
2. There is no qualitative result analysis on the data extraction attacks. It would be better if the authors could conduct these analyses on the data extraction attacks. The lack of qualitative analysis makes it difficult to understand the practical implications of the data extraction attack. For example, are the extracted data points semantically meaningful? Do they correspond to real-world locations or user behaviors? Without this, it's hard to assess the real-world impact of the attack.
3. The threat models assume that the adversaries are capable of accessing the confidence scores, which makes them impractical. In practice, the model owner only releases the final result to the users. In this case, whether the proposed attacks are still effective is unknown. The assumption of access to confidence scores is a significant limitation. Many real-world systems only provide the final prediction, not the underlying confidence values. The paper needs to address how the proposed attacks would perform in more realistic scenarios where only the final prediction is available to the adversary.

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper evaluates the privacy risks of POI recommendation models by introducing an attack suite and conducts extensive experiments to demonstrate the effectiveness of these attacks. Additionally, it analyzes which types of mobility data are vulnerable to the proposed attacks and further adapts two mainstream defense mechanisms to the task of POI recommendation.

### Strengths
S1. The scenario of this paper, POI recommendation, has real-world applications.

S2. The paper proposed several attack methods.

S3. Extensive experiments are conducted on two real datasets.

### Weaknesses
W1. The motivation of this work is not convincing enough. 

W2. The definition of sensitive information is unclear.

W3. Experiments are inadequate and some insights are not surprising.

W4. There are some typos in this paper. For example, at line 16 in algorithm 4,   $f_out$ should be $f_\theta$.

### Questions
Q1. The definition of sensitive information and privacy guarantee should be formally defined and well justified. Then, it may become meaningful to conduct adversary attacks.   
Q2. There have been quite a few studies on protecting spatial/location/trajectory privacy. However, most of them was not reviewed/evaluated by this paper. Thus, it was uncertain whether existing privacy preservation mechanisms could help on the mentioned limitation of POI recommendation.    
Q3. Take private spatial data publish as an example. Based on GDPR, a LBS platform can only collect user’s check-in data that has been well protected (e.g., by differential privacy). Under this practical setting, deriving the platform’s data will not leak the sensitive information of users, which makes the attacker model proposed in this work less meaningful.    
Q4. I am also curious: if the input data has been well protected by existing privacy mechanism and then trained by POI recommendation model, is there any sensitive information leakage?    
Q5. Since privacy preserving learning has been well studied in recent years, it is sometimes possible to extend existing POI recommendation models with privacy guarantee (e.g., by adding differential privacy noise in the gradients). Does this fact significantly change the main insight?   
Q6. In Appendix E, the epsilon setting of DP-SGD is a little large. Please provide more justifications.    
Q7. Both datasets are a little outdated and relatively smaller-scale than the current LBS platform. However, the major insights are strongly related to the data sparsity. Maybe, it would be better to conduct experiments on large-scale datasets.    
Q8. Why does the curve in Figure 5(b) first rise and then drop when the number of POI increases?    
Q9. It is mentioned that k is usually 1, 5, and 10 when using top-k to measure accuracy in page 3. However, only 1, 3, and 5 were tested in the experiment as shown in Figure 1. What is the rationale of this experimental setting?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper offers a privacy attack suite (including data extraction and membership inference attacks) on point-of-interest recommendation models, tailored specifically for mobility data. Experiments are performed on three models trained on two distinct datasets. This suite could in principle be used as a privacy auditing tool.

### Strengths
The paper is very clearly presented and the thoroughness of experimental results is commendable to the point where I am left with view remaining questions. 

The paper demonstrates clear privacy vulnerabilities in POI recommendation systems that should inform future defenses and auditing.

### Weaknesses
It would be valuable to understand how attack vulnerability changes with sample size. For very large datasets, where there are generally a larger number of unique users to all locations, does the attack success decline? This theory seems to be somewhat supported by Fig 4. 

More detailed descriptions of datasets size and dimensionality would be valuable to understand whether the emulate real-world production systems. 

The paper could benefit from explicitly contextualizing how attack performance compares to attack performance for other type of data/models (e.g. text & image are referenced).

### Questions
How do we know if the utility privacy trade-off inherent or a limitation of existing DP algorithms? You note the privacy-utility trade-off does not strictly hold in your experiments but can you show that practically acceptable utility and privacy can both be achieved?

Could you explain why having more total check-ins seems to help protect a user against a MIA? This seems surprising in the context of differential privacy where worst-case privacy loss degrades with sensitivity. 

Have you explored the feasability of DP synthetic data for this type of application?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper emphasizes the importance of assessing privacy risks in mobility data-based ML models. The authors propose a threat model for evaluating privacy risks and provide a comprehensive privacy risk assessment for such models. They also suggest a privacy-preserving solution for point-of-interest recommendation models to mitigate privacy risks. Their contributions include designing four different attacks, such as common location extraction (LOCEXTRACT), training trajectory extraction (TRAJEXTRACT), location-level membership inference attack (LOCMIA), and trajectory-level membership inference attack (TRAJMIA), developing a privacy-preserving training method that protects against data extraction and membership inference attacks aimed at point-of-interest recommendation models. Overall, the authors identify potential privacy risks in mobility data-based machine learning models and propose solutions to address these risks.

### Strengths
1) The paper presents a privacy attack suite that is specifically designed for POI recommendation models. This suite consists of data extraction and membership inference attacks. By conducting experiments with real-world mobility datasets, the authors demonstrate the vulnerability of current POI recommendation models to these attacks.

2) The paper investigates the effectiveness of existing defense mechanisms, such as L2 regularization and differential privacy, against the proposed attacks. However, it concludes that these mechanisms have limitations in providing comprehensive protection.

3) The impact of training and attack parameters on attack performance is analyzed. The effect of training epochs on information leakage and the influence of query timestamps on data extraction attack performance are discussed.

### Weaknesses
1) The study only evaluates the privacy risks of POI recommendation models in a controlled setting. They didn't provide some insights into how these models might perform in real-world scenarios, where more complex factors are at play. Specifically, the paper lacks a discussion on the impact of noisy or incomplete data, which is common in real-world mobility datasets. The attacks are evaluated on datasets that may not fully represent the variability and complexity of real-world user behavior. For example, the datasets might not capture the full range of user mobility patterns, such as infrequent or irregular trips, which could affect the attack performance.

2) The author did not provide insights on how these risks compare to privacy risks associated with ride-sharing or food-delivery apps. The paper does not explore the specific differences in data sensitivity and attack vectors between POI recommendation models and other location-based services. For instance, ride-sharing apps often involve real-time location data and dynamic routes, which could present different privacy challenges compared to the static POI data used in this study. Furthermore, the paper does not discuss how the proposed attacks might be adapted or mitigated in the context of these other services.

### Questions
1) According to the paper, no definitive defense mechanism can protect against all the proposed attacks simultaneously. Can you please explain why this is the case? Additionally, could you provide insights into the challenges that must be addressed to develop more effective defenses against such attacks?

2) How do the proposed attacks and defense mechanisms compare to existing methods in the literature?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
