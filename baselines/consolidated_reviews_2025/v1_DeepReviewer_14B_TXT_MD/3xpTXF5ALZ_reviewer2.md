### Summary

This paper proposes a deep learning-based approach for email phishing attack localization, which can automatically learn and identify the most important and phishing-relevant information in phishing emails, offering useful and concise explanations for the identified vulnerability. The proposed approach works effectively in a weakly supervised setting, providing an important practical solution for defeating phishing attacks. The extensive experiments on seven diverse real-world email datasets demonstrate the effectiveness and superiority of the proposed method over the state-of-the-art baselines.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The proposed method can provide concise and meaningful interpretations to the users, which is very important in real-world applications.
2. The proposed method works effectively in a weakly supervised setting, which is an important practical solution for defeating phishing attacks.
3. The extensive experiments on seven diverse real-world email datasets demonstrate the effectiveness and superiority of the proposed method over the state-of-the-art baselines.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is only evaluated on email datasets, which may not be representative of all types of phishing attacks. For example, phishing attacks through social media platforms or other communication channels may have different characteristics and require different approaches. The method's reliance on email-specific features, such as the structure of email headers and the typical flow of email content, may not translate well to other modalities. For instance, social media phishing often relies on visual cues and shortened URLs, which are absent in email-based attacks. This limits the generalizability of the proposed approach.
2. The proposed method may not be able to handle new or unknown types of phishing attacks that are not seen during training. The model's performance is likely to degrade when presented with novel attack patterns or techniques that deviate significantly from the training data. This is a common challenge in machine learning, but it is particularly relevant in the context of phishing, where attackers are constantly evolving their strategies. The lack of robustness to unseen attacks is a significant limitation.
3. The proposed method may require a large amount of labeled data for training, which may be difficult to obtain in practice, especially for new or emerging types of phishing attacks. While the paper mentions weak supervision, the quality and quantity of weak labels can still impact the model's performance. Furthermore, the process of obtaining even weak labels for diverse phishing attacks can be time-consuming and resource-intensive. The reliance on labeled data, even if weakly labeled, remains a practical challenge.

### Suggestions

To address the limitations of the proposed method, several improvements could be considered. First, the model should be evaluated on a more diverse set of phishing datasets that include attacks from various communication channels, such as social media, instant messaging, and SMS. This would provide a more comprehensive assessment of the method's generalizability and robustness. Specifically, the evaluation should include datasets that contain phishing attacks with different characteristics, such as those relying on visual cues, shortened URLs, or social engineering tactics that are not specific to email. Furthermore, the model should be tested on datasets that include attacks from different languages and regions to ensure its applicability across different contexts. This would help to identify the specific weaknesses of the model and guide the development of more robust and generalizable solutions.

Second, the method should be enhanced to handle new or unknown types of phishing attacks. This could be achieved by incorporating techniques such as anomaly detection or few-shot learning, which can enable the model to identify and adapt to novel attack patterns. For example, the model could be trained to detect deviations from normal communication patterns or to learn from a small number of examples of new attack types. Additionally, the model could be designed to incorporate external knowledge sources, such as threat intelligence feeds, to stay updated on the latest phishing tactics and techniques. This would help to improve the model's ability to detect emerging threats and reduce its reliance on historical data. The use of adversarial training could also be explored to make the model more robust to variations in attack patterns.

Finally, the reliance on labeled data should be reduced by exploring self-supervised or unsupervised learning techniques. These techniques can enable the model to learn from unlabeled data, which is often more abundant and easier to obtain than labeled data. For example, the model could be trained to reconstruct email content or to predict the next word in a sequence, which can help it to learn useful representations of email data without requiring labeled examples. Furthermore, the model could be designed to incorporate domain knowledge or to use transfer learning to leverage pre-trained models that have been trained on large datasets. This would help to reduce the need for large amounts of labeled data and improve the model's performance on new or emerging types of phishing attacks.

### Questions

1. How does the proposed method perform on other types of phishing attacks, such as those through social media platforms or other communication channels?
2. How does the proposed method handle new or unknown types of phishing attacks that are not seen during training?
3. How does the proposed method perform with limited labeled data, and how can the amount of labeled data required for training be reduced?

### Rating

3

### Confidence

3

**********
