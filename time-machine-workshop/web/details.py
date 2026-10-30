"""Click-for-detail content for the web deck, drawn from the wallet evolution research report."""

REPORT = "https://github.com/ademiroliveira/SC-IA/blob/main/time-machine-workshop/wallet-evolution-research.md"

S = {
    "walletconnect": ("Coin Bureau: what is WalletConnect", "https://coinbureau.com/technology/what-is-walletconnect"),
    "blind": ("Ledger Academy: blind signing explained", "https://www.ledger.com/academy/cryptos-greatest-weakness-blind-signing-explained"),
    "clear": ("Ledger Academy: what is clear signing", "https://www.ledger.com/academy/topics/ledgersolutions/what-is-clear-signing"),
    "chainalysis": ("Chainalysis: crypto hacking and stolen funds", "https://www.chainalysis.com/blog/crypto-hacking-stolen-funds-2026/"),
    "turnkey": ("Turnkey: ERC-4337 and EIP-7702", "https://www.turnkey.com/blog/account-abstraction-erc-4337-eip-7702"),
    "fireblocks": ("Fireblocks: the Bybit attack", "https://www.fireblocks.com/blog/bybit-attack-security-flaws-fireblocks-nation-state-resilient-solutions"),
    "zerotrace": ("Zero Trace Labs: the Bybit blind-signing hack", "https://zerotracelabs.xyz/bybit-multisig-blind-signing-hack-a-1-5-billion-supply-chain-compromise-via-safe-wallet-frontend-manipulation/"),
    "coinbase": ("Coinbase: Agentic Wallets", "https://www.coinbase.com/developer-platform/discover/launches/agentic-wallets"),
    "efclear": ("BeInCrypto: Ethereum Foundation launches Clear Signing", "https://beincrypto.com/ethereum-foundation-launches-clear-signing-standard/"),
    "cryptonomist": ("Cryptonomist: Ethereum Clear Signing and ERC-7730", "https://en.cryptonomist.ch/2026/05/13/ethereum-clear-signing-erc-7730/"),
    "scamsniffer": ("Scam Sniffer: 2025 phishing losses report", "https://drops.scamsniffer.io/scam-sniffer-2025-crypto-phishing-losses-fall-83-to-84-million/"),
    "coincentral83": ("CoinCentral: phishing losses fall to $83M in 2025", "https://coincentral.com/scam-sniffer-crypto-phishing-losses-fall-to-83m-in-2025/"),
    "hogedark": ("Hoge: the dark side of EIP-7702", "https://hoge.gg/eip-7702-smart-account-dark-side-2026/"),
    "spark7702": ("Spark: EIP-7702 code delegation", "https://www.spark.money/research/ethereum-eip-7702-code-delegation-wallets"),
    "fusaka": ("TradingView: how the Fusaka upgrade fits Ethereum’s roadmap", "https://www.tradingview.com/news/cointelegraph:3f90403a9094b:0-how-the-fusaka-upgrade-fits-into-ethereum-s-long-term-roadmap/"),
    "waas": ("Upshift: wallet-as-a-service providers", "https://www.upshift.finance/blog/wallet-as-a-service-providers"),
    "thn": ("The Hacker News: Trust Wallet Chrome extension hack", "https://thehackernews.com/2025/12/trust-wallet-chrome-extension-hack.html"),
    "twak": ("Trust Wallet: introducing the Agent Kit", "https://trustwallet.com/blog/company/introducing-the-trust-wallet-agent-kit-twak-your-ai-agent-can-now-act-on-crypto"),
    "bankless": ("Bankless: MetaMask launches agent wallets", "https://www.bankless.com/read/news/metamask-launches-agent-wallets"),
    "bnc": ("BraveNewCoin: x402 records 138.5M transactions", "https://bravenewcoin.com/insights/coinbases-x402-records-138-5m-transactions-chainalysis-shows-ai-agents-reshaping-crypto-payments"),
    "coincentralx402": ("CoinCentral: x402 passes 138 million transactions", "https://coincentral.com/ai-agents-gain-ground-as-x402-passes-138-million-transactions214628-2"),
}

DETAILS = {
    "m2009": {
        "eyebrow": "2009",
        "title": "Keys in a file",
        "body": [
            "The original Bitcoin client was a full node with a built-in wallet. Private keys sat in one file, wallet.dat, and encryption only arrived in 2011.",
            "Backups went stale, because change went to new keys that an old backup did not contain. The user was the backup system.",
        ],
        "sources": [],
    },
    "seed": {
        "eyebrow": "2012–2014",
        "title": "HD wallets and seed phrases",
        "body": [
            "BIP32 (2012) let one master seed derive a whole tree of keys. BIP39 (2013) wrote that seed as 12 to 24 words, and BIP44 (2014) standardized the paths across coins and accounts.",
            "It gave people one backup that works across wallets, which made a competitive wallet market possible. It also turned the seed phrase into a bearer instrument and the main phishing target.",
        ],
        "sources": [],
    },
    "m2014": {
        "eyebrow": "2014",
        "title": "Hardware wallets and Mt. Gox",
        "body": [
            "Trezor shipped the first commercial hardware wallet in 2014, and Ledger followed with secure-element devices. Keys left the computer.",
            "The same year Mt. Gox collapsed, and “not your keys, not your coins” became the ethos of the next decade.",
        ],
        "sources": [],
    },
    "hardware": {
        "eyebrow": "2012–2014",
        "title": "Hardware wallets",
        "body": [
            "Trezor shipped in 2014 with open-source firmware; Ledger used secure-element chips. Later devices added air-gapped signing through QR codes, microSD cards and partially signed Bitcoin transactions.",
            "The value has moved from “keys are offline” to “the trusted display is the source of truth”: a device only protects you if it can show what it is signing.",
        ],
        "sources": ["blind", "clear"],
    },
    "exchanges": {
        "eyebrow": "2012–2014",
        "title": "Exchange failures",
        "body": [
            "Mt. Gox (2014), QuadrigaCX (2019), and Celsius and FTX (2022) each strengthened the case for self-custody. FTX’s failure drove hardware wallet sales and withdrawals.",
            "Custody risk did not disappear; it moved. Chainalysis counted $3.4B stolen in 2025, dominated by the Bybit service compromise.",
        ],
        "sources": ["chainalysis"],
    },
    "login": {
        "eyebrow": "2016–2018",
        "title": "MetaMask and WalletConnect",
        "body": [
            "With MetaMask (2016) the wallet stopped being only a payment tool and became the login and approval layer for every app. WalletConnect (2018) did the same for mobile through QR-code sessions.",
            "WalletConnect now reports more than 700 wallets and 80,000 apps. Understanding what you sign became the main UX problem.",
        ],
        "sources": ["walletconnect"],
    },
    "m2022": {
        "eyebrow": "2022",
        "title": "FTX",
        "body": [
            "FTX’s collapse in November 2022 took self-custody from a niche preference to a mainstream argument, and drove hardware wallet sales and withdrawals.",
        ],
        "sources": [],
    },
    "erc4337": {
        "eyebrow": "2023",
        "title": "ERC-4337 smart accounts",
        "body": [
            "ERC-4337 went live in March 2023. It standardized smart accounts without changing Ethereum itself, using bundlers and paymasters that can sponsor gas.",
            "Session keys and modular standards then made scoped, expiring permissions possible. A late-August 2026 summary of BundleBear data cited about 65 million active accounts.",
        ],
        "sources": ["turnkey"],
    },
    "m2025": {
        "eyebrow": "2025",
        "title": "EIP-7702 and Bybit",
        "body": [
            "EIP-7702 went live with Ethereum’s Pectra upgrade on May 7, 2025. It lets an existing address act as a smart account without changing address.",
            "Earlier that year, on February 21, Bybit lost about $1.46B through a tampered signing interface and blind signing on hardware wallets.",
        ],
        "sources": ["turnkey", "fireblocks"],
    },
    "m2026": {
        "eyebrow": "2026",
        "title": "Agent wallets and Clear Signing",
        "body": [
            "Coinbase and Phantom (February), Trust Wallet (March) and MetaMask (August) shipped agent wallets or agent tooling.",
            "The Ethereum Foundation launched Clear Signing on May 12, 2026, with a working group spanning MetaMask, Ledger, Trezor, Fireblocks and WalletConnect.",
        ],
        "sources": ["coinbase", "efclear"],
    },
    "lostbtc": {
        "eyebrow": "Lost bitcoin",
        "title": "About 20% of bitcoin is probably lost",
        "body": [
            "In June 2020 Chainalysis estimated that about 3.7M BTC, roughly 20% of the supply mined by then, had not moved in at least five years and was probably lost. Its 2017 estimate was 17 to 23%. Decrypt reported the 2020 figure.",
            "It is an estimate, not a count. It is the clearest picture of what “the user is the backup system” costs.",
        ],
        "sources": [],
    },
    "approvals": {
        "eyebrow": "2016–2024",
        "title": "Token approvals",
        "body": [
            "Token approvals (often unlimited), NFT operator approvals and off-chain Permit signatures let one signature authorize future transfers.",
            "Scam Sniffer recorded the largest single drainer theft of 2025 as a $6.5 million Permit-based theft, down from a $55.4M largest case in 2024.",
        ],
        "sources": ["scamsniffer"],
    },
    "clearsign": {
        "eyebrow": "2016–2024",
        "title": "Clear signing",
        "body": [
            "Transaction simulation previews how your balances will change. Ledger’s ERC-7730 standard (2024) uses metadata to show contract calls in plain language; version 2 shipped in April 2026 and the Ethereum Foundation now stewards it.",
            "It only works when both the wallet and the app support it, and simulation itself can be spoofed.",
        ],
        "sources": ["clear", "cryptonomist"],
    },
    "drainers": {
        "eyebrow": "Drainer phishing losses",
        "title": "$494M in 2024, $83.85M in 2025",
        "body": [
            "Scam Sniffer counted about $494M stolen from about 332,000 victims in 2024, and $83.85M from 106,106 victims in 2025: an 83% drop. Only 11 thefts exceeded $1M, against 30 the year before.",
            "Scam Sniffer ties the drop mainly to lower market activity, and warns it may partly reflect a shift to attacks that are harder to track. Do not read it as proof that wallet protections worked.",
        ],
        "sources": ["scamsniffer", "coincentral83"],
    },
    "eip7702": {
        "eyebrow": "2025",
        "title": "EIP-7702",
        "body": [
            "Since May 2025 an existing address can sign an authorization that points it to a smart-account implementation, keeping the same address and key. Major wallets integrated it.",
            "Adoption is contested: trackers counted 45 to 60 million live delegations by August and September 2026, but much of that comes from attackers’ sweeper bots. “Upgrade your account” is now a prompt that phishers imitate.",
        ],
        "sources": ["hogedark", "spark7702"],
    },
    "passkeys": {
        "eyebrow": "2023–2025",
        "title": "Passkeys and embedded wallets",
        "body": [
            "Passkeys keep keys in a phone’s secure hardware. Coinbase Smart Wallet made passkey accounts mainstream in 2024, and Ethereum’s Fusaka upgrade (December 2025) made passkey signatures cheap to verify.",
            "Embedded wallets create an account at email or social login, and the vendors consolidated: Stripe bought Privy and Fireblocks bought Dynamic in 2025. The trade-off is dependence on Apple, Google or the provider for recovery.",
        ],
        "sources": ["fusaka", "waas"],
    },
    "bybit": {
        "eyebrow": "February 2025",
        "title": "Bybit: about $1.46B",
        "body": [
            "The Safe Ecosystem Foundation traced the attack to a compromised developer machine that proposed a disguised malicious transaction. Its review found no flaw in the Safe contracts.",
            "Signers saw what looked like a routine transfer. Their hardware wallets could not decode the payload, so they were blind signing. The interface, not the key, was the weakest link.",
        ],
        "sources": ["fireblocks", "zerotrace"],
    },
    "supplychain": {
        "eyebrow": "2023–2025",
        "title": "Supply chain",
        "body": [
            "Trust Wallet’s Chrome extension version 2.68 was trojanized after the Shai-Hulud npm worm exposed GitHub secrets and a Chrome Web Store publishing key: about $8.5M from 2,520 wallets.",
            "In December 2023 a compromised Ledger Connect Kit package injected a drainer into the apps that used it. Users who did everything right were hit.",
        ],
        "sources": ["thn"],
    },
    "agentwallets": {
        "eyebrow": "2026",
        "title": "Agent wallets",
        "body": [
            "Coinbase Agentic Wallets (February 2026) keep keys in isolated hardware, with session caps and per-transaction limits. Trust Wallet’s Agent Kit (March) offers rule-bound agent wallets, or “agent proposes, user approves”.",
            "MetaMask’s Agent Wallet (generally available in August) adds daily limits, protocol allowlists and a Guard Mode that asks a person when an action falls outside the rules. The first documented prompt-injection theft from an agent wallet came in May 2026.",
        ],
        "sources": ["coinbase", "twak", "bankless"],
    },
    "x402": {
        "eyebrow": "Agent payments",
        "title": "138M agent payments on Base",
        "body": [
            "x402 lets software agents pay small amounts in stablecoins over the web. It grew from about 1,500 transactions in mid-2025 to more than 138 million on Base by Q3 2026, according to Chainalysis. 87% of payments are under $0.10.",
            "Other trackers report different totals, and wash trading could inflate the volume. Treat it as directional: agents are already moving money.",
        ],
        "sources": ["bnc", "coincentralx402"],
    },
    "open-recovery": {
        "eyebrow": "Open problem 01",
        "title": "Recovery",
        "body": [
            "There is still no universally trusted, portable, non-custodial way to recover a wallet.",
            "Each option moves the risk: seed phrases are fragile, guardians are a social burden, cloud passkeys depend on Apple or Google, and provider-held key shares sit close to custody.",
        ],
        "sources": [],
    },
    "open-signing": {
        "eyebrow": "Open problem 02",
        "title": "Signing comprehension",
        "body": [
            "Clear signing (ERC-7730) only works when both the wallet and the app support it.",
            "Typed data, batched calls, account delegations and intents are each harder to explain than a simple transfer.",
        ],
        "sources": [],
    },
    "open-supply": {
        "eyebrow": "Open problem 03",
        "title": "Supply chain",
        "body": [
            "The Bybit front end, Trust Wallet’s extension and Ledger Connect Kit show that auto-updating front ends and browser extensions are the new single points of failure.",
        ],
        "sources": [],
    },
    "open-delegation": {
        "eyebrow": "Open problem 04",
        "title": "Delegation sprawl",
        "body": [
            "Token allowances, account delegations, session keys and agent grants are piling up.",
            "Few wallets give one understandable view of everything that can act on your behalf, with a one-tap revoke.",
        ],
        "sources": [],
    },
    "open-crosschain": {
        "eyebrow": "Open problem 05",
        "title": "Cross-chain complexity",
        "body": [
            "Every new chain adds address formats, gas tokens, bridges and network prompts. It is now the largest source of friction that is not about security.",
            "Chain abstraction removes steps but moves trust to the solvers that route the transactions.",
        ],
        "sources": [],
    },
}

# Which element on which slide opens which detail: (slide id, exact element text, detail key).
MARKS = [
    ("milestones", "2009", "m2009"),
    ("milestones", "2012–13", "seed"),
    ("milestones", "2014", "m2014"),
    ("milestones", "2016–18", "login"),
    ("milestones-late", "2022", "m2022"),
    ("milestones-late", "2023", "erc4337"),
    ("milestones-late", "2025", "m2025"),
    ("milestones-late", "2026", "m2026"),
    ("keys", "Seed phrases", "seed"),
    ("keys", "Hardware wallets", "hardware"),
    ("keys", "Exchange failures", "exchanges"),
    ("keys-stat", "About 20%", "lostbtc"),
    ("approval", "Wallet as login", "login"),
    ("approval", "Token approvals", "approvals"),
    ("approval", "Clear signing", "clearsign"),
    ("approval-stat", "$494M", "drainers"),
    ("approval-stat", "$83.85M", "drainers"),
    ("accounts", "ERC-4337, 2023", "erc4337"),
    ("accounts", "EIP-7702, 2025", "eip7702"),
    ("accounts", "Passkeys", "passkeys"),
    ("agents", "Bybit, 2025", "bybit"),
    ("agents", "Supply chain", "supplychain"),
    ("agents", "Agent wallets", "agentwallets"),
    ("agents-stat", "$1.46B", "bybit"),
    ("agents-stat", "138M", "x402"),
    ("open", "Recovery", "open-recovery"),
    ("open", "Signing comprehension", "open-signing"),
    ("open", "Supply chain", "open-supply"),
    ("open", "Delegation sprawl", "open-delegation"),
    ("open", "Cross-chain complexity", "open-crosschain"),
]


def resolved():
    """DETAILS with source keys replaced by (label, url) pairs."""
    out = {}
    for key, d in DETAILS.items():
        out[key] = dict(d, sources=[list(S[s]) for s in d["sources"]])
    return out
