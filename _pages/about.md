---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>
Yanbo Wang is currently a Research Intern at [MBZUAI](https://mbzuai.ac.ae/), supervised by [Prof. Xiuying Chen](https://iriscxy.github.io/). I also collaborate with MINE Lab at the University of Notre Dame, under the guidance of [Prof. Xiangliang Zhang](https://sites.nd.edu/xiangliang-zhang/) and in close collaboration with [Yue Huang (PhD Candidate)](https://howiehwong.github.io/), which has been an incredibly rewarding experience. My research interests include LLM Reasoning and Generative Foundation Models.

<!-- Dynamic GitHub stars badge for all repositories -->
[![GitHub stars](https://img.shields.io/github/stars/wyf23187?style=social)](https://github.com/wyf23187)

> I am actively seeking a PhD position starting in Fall 2026.

# 🔥 News
- *2025.01*: &nbsp;🎉🎉 One paper has been accepted by **ICLR 2025**. Congratulations to Jiayi and [Yue](https://howiehwong.github.io/)!
- *2024.09*: &nbsp;🎉🎉 Two papers have been accepted by NeurIPSW 2024!

# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2025</div><img src='images/llm-judge-bias.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge](https://arxiv.org/abs/2410.02736)

Jiayi Ye\*, **Yanbo Wang**\*, Yue Huang\*, Dongping Chen, Qihui Zhang, Pin-Yu Chen, Nitesh V. Chawla, Xiangliang Zhang (\*: Equal contribution)

[![Website Visits](https://img.shields.io/badge/Github-Website-blue?style=flat&logo=github&logoColor=white)](https://llm-judge-bias.github.io/)
[![Arxiv](https://img.shields.io/badge/Paper-Arxiv-red)](https://arxiv.org/abs/2410.02736)
[![Paper](https://img.shields.io/badge/Paper-PDF-blue)](https://arxiv.org/pdf/2410.02736)

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">In submission</div><img src='images/CDV.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Breaking Focus: Contextual Distraction Curse in Large Language Models](https://arxiv.org/abs/2502.01609)

**Yanbo Wang**\*, Zixiang Xu\*, Yue Huang\*, Chujie Gao, Siyuan Wu, Jiayi Ye, Xiuying Chen, Pin-Yu Chen, Xiangliang Zhang (\*: Equal contribution)

[![Arxiv](https://img.shields.io/badge/Paper-Arxiv-red)](https://arxiv.org/abs/2502.01609)
[![Paper](https://img.shields.io/badge/Paper-PDF-blue)](https://arxiv.org/pdf/2502.01609)
[![Github](https://img.shields.io/badge/Code-Github-green)](https://github.com/wyf23187/LLM_CDV)

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Accepted at NAACL 2025 Demo</div><img src='images/trusteval.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[TRUSTEVAL: A Dynamic Evaluation Toolkit on Trustworthiness of Generative Foundation Models](https://trustgen.github.io/)

**Yanbo Wang**\*, Jiayi Ye\*, Siyuan Wu\*, Chujie Gao, Yue Huang, Xiuying Chen, Yue Zhao, Xiangliang Zhang (\*: Equal contribution)

[![Website Visits](https://img.shields.io/badge/Github-Website-blue?style=flat&logo=github&logoColor=white)](https://trustgen.github.io/)
[![Github](https://img.shields.io/badge/Code-Github-green)](https://github.com/nauyisu022/TrustEval-toolkit)

</div>
</div>

- [UPME: An Unsupervised Peer Review Framework for Multimodal Large Language Model Evaluation](https://arxiv.org/abs/2503.14941)
  Qihui Zhang, Munan Ning, Zheyuan Liu, **Yanbo Wang**, Jiayi Ye, Yue Huang, Shuo Yang, Xiao Chen, Yibing Song, Li Yuan  
  **Accepted at CVPR 2025**  
  [![Arxiv](https://img.shields.io/badge/Paper-Arxiv-red)](https://arxiv.org/abs/2503.14941)
  [![Paper](https://img.shields.io/badge/Paper-PDF-blue)](https://arxiv.org/pdf/2503.14941)

- [Cross-Lingual Pitfalls: Automatic Probing Cross-Lingual Weakness of Multilingual Large Language Models](https://arxiv.org/)
  Zixiang Xu\*, **Yanbo Wang**\*, Yue Huang\*, Xiuying Chen, Jieyu Zhao, Meng Jiang, Xiangliang Zhang (\*: Equal contribution)  
  **In submission**  
  [![Github](https://img.shields.io/badge/Code-Github-green)](https://github.com/xzx34/Cross-Lingual-Pitfalls)

- [On the Trustworthiness of Generative Foundation Models: Guideline, Assessment, and Perspective](https://arxiv.org/abs/2502.14296)
  Yue Huang, Chujie Gao, Siyuan Wu, Haoran Wang, Xiangqi Wang, Yujun Zhou, **Yanbo Wang**, Jiayi Ye, Jiawen Shi, Zhaoyi Liu, Tianrui Guan, Dongping Chen, Ruoxi Chen, etc.
  [![Arxiv](https://img.shields.io/badge/Paper-Arxiv-red)](https://arxiv.org/abs/2502.14296)
  [![Paper](https://img.shields.io/badge/Paper-PDF-blue)](https://arxiv.org/pdf/2502.14296)
  [![Website](https://img.shields.io/badge/Website-Visit-blue)](https://trustgen.github.io/)
  [![Docs](https://img.shields.io/badge/Documentation-Read-green)](https://trusteval-docs.readthedocs.io)
  [![Demo](https://img.shields.io/badge/Demo-YouTube-red)](https://www.youtube.com/@TrustEval)
  [![Github](https://img.shields.io/badge/Toolkit-Github-green)](https://github.com/TrustGen/TrustEval-toolkit)

- [AutoBench-V: Can Large Vision-Language Models Benchmark Themselves?](https://arxiv.org/abs/2410.21259)
  Han Bao\*, Yue Huang\*, **Yanbo Wang**\*, Jiayi Ye\*, Xiangqi Wang, Xiuying Chen, Mohamed Elhoseiny, Xiangliang Zhang (\*: Equal contribution)  
  **Accepted at SFLLM Workshop @ NeurIPS 2024**  
  [![Website Visits](https://img.shields.io/badge/Github-Website-blue?style=flat&logo=github&logoColor=white)](https://autobench-v.github.io/)
  [![Arxiv](https://img.shields.io/badge/Paper-Arxiv-red)](https://arxiv.org/abs/2410.21259)
  [![Paper](https://img.shields.io/badge/Paper-PDF-blue)](https://arxiv.org/pdf/2410.21259)

# 🎖 Honors and Awards
- *2024.10* 2nd Place, IEEE CS North America Student Challenge 2024 (Kaggle)
- *2024.10* Bronze Medal, The 2024 CCF CCSP National Programming Contest
- *2024.06* Gold Medal (Second Place), The 16th ICPC Sichuan Provincial Collegiate Programming Contest
- *2024.05* Silver Medal, The 2024 ICPC China Wuhan National Invitational Contest Wuhan University

# 💻 Internships
- *2024.07 - now*, Research Intern at <img src='images/Notre_Dame.jpg' style='width: 1.2em;'> [University of Notre Dame](https://www.nd.edu/) 

<a href="https://mapmyvisitors.com/web/1bwe4"  title="Visit tracker"><img src="https://mapmyvisitors.com/map.png?d=vnKG7xcmb4-m1Z1kMj0BL_A6UV7TA7ap7MLUKPmjtuc&cl=ffffff" /></a>