# hello-kicktty-ai-server
헬로킥티 AI 서버입니다. 

## [필수] hello-kicktty 환경 설정
- `hello-kicktty-ai` 환경 안에서 작업해주세요.
1. conda 환경 생성
    ```bash
    # conda 환경 생성
    conda create -n hello-kicktty-ai python=3.11.5
    ```
2. hello-kicktty-ai 환경 활성화
    ```bash
    # hello-kicktty-ai 환경 활성화
    conda activate hello-kitty-ai
    ```
3. requirements.txt 연동
    ```bash
    # requirements.txt 연동
    pip install -r requirements.txt
    ```

## requirements 백업
```bash
pip list --format=freeze > requirements.txt
```

## 서버 시작
```bash
sh start.sh
```