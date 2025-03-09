async function initializeHashConnect(hashconnectData) {
    const hashconnect = new Hashconnect();
    const appMetadata = {
        name: "Hedera Flask App",
        description: "A scalable Flask app with Hedera",
        icon: "https://example.com/icon.png"
    };

    const initData = await hashconnect.init(appMetadata, hashconnectData.topic, true);
    hashconnect.foundExtensionEvent.on((walletMetadata) => {
        console.log("Wallet extension found:", walletMetadata);
    });

    hashconnect.pairingEvent.on((pairingData) => {
        const accountId = pairingData.accountIds[0];
        document.getElementById("hashconnect-status").innerText = "Paired with wallet: " + accountId;
        fetch('/hedera/set-account', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ account_id: accountId })
        }).then(() => window.location.href = '/auth/dashboard');
    });

    await hashconnect.connectToLocalWallet();
}