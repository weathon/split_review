### Summary

This paper proposes a formalization of experimental studies, their results, and of similarity between results, in order to provide a quantifiable notion of generalizability of experimental studies.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

The problem studied in this paper is quite important. The formalization of experimental studies and their results provided in this paper is quite novel. The distinction between ideal and empirical studies is quite reasonable.

### Weaknesses

#### Some Related Works


#### comment

1. The definitions of ideal and empirical studies seem to be problematic. In my opinion, the ideal study is just a theoretical concept, which cannot be directly used to conduct experiments. Only empirical studies can be used to conduct experiments. The definition of the result of an ideal study also relies on the ideal experiment function E, which is also not directly observable in practice. In fact, what we care about about is the true experiment function E, but the definition in this paper is quite different from it.

2. The generalizability defined in this paper is also problematic. Firstly, the generalizability is defined for ideal studies, rather than empirical studies. In fact, the generalizability of ideal studies cannot be directly used to guide our practice. We should care about the generalizability of empirical studies, rather than ideal studies. Secondly, the definition of generalizability in this paper is defined for studies with the same goals, rather than the same research question. As indicated in Definition 3.2, the research question is defined to include the goals. Thus, it is quite confusing that why the generalizability is not defined for studies with the same research question. Thirdly, the definition of generalizability in this paper relies on the unknown probability distribution P, which cannot be directly estimated in practice.

3. The contribution 3 claimed in this paper is problematic. This paper provides no theoretical or experimental evidence to show how the developed algorithm can be used to determine the appropriate size of a study.

4. The presentation of this paper can be improved. The introduction section should provide some concrete examples to illustrate the problem studied in this paper. This would be helpful for readers to better understand the problem. The contribution 2 claimed in this paper should be described more explicitly, rather than just stating "we propose a quantifiable definition of the generalizability of experimental studies". The contribution 2 can be better described by specifically pointing out the differences between the proposed generalizability and previous related concepts, such as the replicability and generalizability given in Pineau et al. (2021) and National Academies of Science, 2019, as well as the model replicability defined in Impagliazzo et al. (2022).

### Suggestions

The paper's core issue lies in its definition of 'ideal' and 'empirical' studies, which are not clearly distinguished in practice. The 'ideal' study, as defined, appears to be a theoretical construct rather than a practical entity that can be directly studied or experimented upon. The paper defines the result of an ideal study based on an 'ideal' experiment function E, which is not directly observable. This raises concerns about the practical relevance of the proposed framework. The paper should clarify how this 'ideal' function relates to the true experiment function that practitioners care about. Furthermore, the generalizability defined for ideal studies is problematic because it does not directly address the generalizability of empirical studies, which are the actual objects of experimental research. The paper needs to bridge the gap between the theoretical ideal and the practical empirical, providing a clear explanation of how the proposed generalizability measure for ideal studies can be used to guide the design and interpretation of empirical studies.

The definition of generalizability is also problematic because it is defined for studies with the same goals, rather than the same research question. The paper defines the research question to include the goals, making it unclear why generalizability is not defined for studies with the same research question. This distinction is crucial because research questions often encompass more than just the goals of the study. The paper should clarify the relationship between research questions and goals, and explain why the generalizability is defined for studies with the same goals. Moreover, the generalizability definition relies on an unknown probability distribution P, which cannot be directly estimated in practice. The paper should provide a practical method for estimating this distribution or justify why it is not necessary. The paper should also provide a more concrete explanation of how the proposed algorithm can be used to determine the appropriate size of a study, as the current contribution lacks both theoretical and experimental evidence.

Finally, the presentation of the paper needs significant improvement. The introduction should include concrete examples to illustrate the problem being studied, which would help readers better understand the motivation and relevance of the work. The paper should also describe the contributions more explicitly, particularly the second contribution, which is currently too vague. Instead of simply stating that the paper proposes a quantifiable definition of generalizability, the paper should clearly point out the differences between the proposed definition and previous related concepts, such as replicability and generalizability as defined in prior work. This would help readers understand the novelty and significance of the proposed approach. The paper should also provide a more detailed explanation of how the proposed framework can be used in practice, including specific steps and considerations for applying the generalizability measure to real-world experimental studies.

### Questions

Please see the weaknesses.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
