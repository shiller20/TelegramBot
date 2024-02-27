from faulthandler import disable
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram import InputMediaPhoto, ParseMode
from telegram.ext.dispatcher import run_async

import requests
import json

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import  CallbackQueryHandler, CommandHandler, ContextTypes, ConversationHandler
import telegram
from web3 import Web3
import time
import web3
from solcx import compile_standard
from solcx import compile_source
import solcx
import urllib.request
import urllib.parse

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from eth_account.messages import defunct_hash_message, encode_defunct, _hash_eip191_message

solcx.install_solc('0.8.8')

w3 = Web3(Web3.HTTPProvider('https://eth-goerli.g.alchemy.com/v2/hQK0MvpB-2ImSBRwfrAaPv0JdqDIEGVv'))
# w32 = Web3(Web3.HTTPProvider('https://rpc.mevblocker.io'))

bot_token = '5934849173:AAFwSsdgIf1c_1waL2Mg1e07Gd7ZM4TX1kU'
botee = telegram.Bot(token=bot_token)
updater = Updater(token=bot_token, use_context=True)

# Define a dictionary to store the user details
user_details = {}
wid = []
pkeys = {}
accounts = {}
tokenames = {}
contract = {}
supplys = {}
#enablet = {}
socials = {}
ssymbols = {}


def start(update, context):
    if int(update.message.chat_id) in wid:
        update.message.reply_text('Hi there! Let\'s create your token. What is the name of your token?')
        return 'TOKEN_NAME'
    else :
        update.message.reply_text('🖕')

def get_token_name(update, context):
    user_details[update.message.chat_id] = {}
    user_details[update.message.chat_id]['token_name'] = update.message.text
    update.message.reply_text('Great! What is the symbol of your token?')
    return 'TOKEN_SYMBOL'

def get_token_symbol(update, context):
    user_details[update.message.chat_id]['token_symbol'] = update.message.text
    update.message.reply_text('Nice! What is the initial supply of your token?')
    return 'TOKEN_SUPPLY'

def get_token_supply(update, context):
    user_details[update.message.chat_id]['token_supply'] = update.message.text
    update.message.reply_text('marketing wallet ?')
    return 'MW'




def get_mw(update, context):
    user_details[update.message.chat_id]['mw'] = update.message.text


    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text='Confirm Deployment', callback_data='jeje')]])

    try:
        so = socials[update.message.chat_id]
    except:
        so = "-"

    texti='<b>Here are the details of your token:</b>\n' + 'Token Name: ' + user_details[update.message.chat_id]['token_name'] + '\n' +'Token Symbol: ' + user_details[update.message.chat_id]['token_symbol'] + '\n' +'Token Supply: ' + user_details[update.message.chat_id]['token_supply'] + '\n' +'Marketing Wallet: ' + user_details[update.message.chat_id]['mw'] +'\n' + 'Socials: ' + so
    botee.send_message(text=texti,chat_id=update.message.chat_id,reply_markup=reply_markup,parse_mode=ParseMode.HTML)
    return ConversationHandler.END








def cancel(update, context):
    update.message.reply_text('Conversation cancelled.')
    return ConversationHandler.END

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('deploy', start)],
    states={
        'TOKEN_NAME': [MessageHandler(Filters.text & ~Filters.command, get_token_name)],
        'TOKEN_SYMBOL': [MessageHandler(Filters.text & ~Filters.command, get_token_symbol)],
        'TOKEN_SUPPLY': [MessageHandler(Filters.text & ~Filters.command, get_token_supply)],
        'MW': [MessageHandler(Filters.text & ~Filters.command, get_mw)],

    },
    fallbacks=[CommandHandler('cancel', cancel)]
)




cabi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_maxTxAmount","type":"uint256"}],"name":"MaxTxAmountUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"ManualSwap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"_maxTaxSwap","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_maxTxAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_maxWalletSize","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_taxSwapThreshold","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"openTrading","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"removeLimits","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"transferDelayEnabled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'

def seta(update: Update, context: CallbackContext):
    user_message = update.message.text
    cmd_first = '/address '
    user_message1 = user_message.replace(cmd_first, '')
    accounts[update.effective_chat.id] = user_message1
    botee.send_message(chat_id=update.effective_chat.id ,text=f'<i>Address is set</i>', parse_mode=ParseMode.HTML)


def setp(update: Update, context: CallbackContext):
    user_message = update.message.text
    cmd_first = '/pkey '
    user_message1 = user_message.replace(cmd_first, '')
    pkeys[update.effective_chat.id] = user_message1
    botee.send_message(chat_id=update.effective_chat.id ,text=f'<i>Private Key is set</i>', parse_mode=ParseMode.HTML)


def setso(update: Update, context: CallbackContext):
    user_message = update.message.text
    cmd_first = '/socials '
    user_message1 = user_message.replace(cmd_first, '')
    socials[update.effective_chat.id] = user_message1
    botee.send_message(chat_id=update.effective_chat.id ,text=f'<i>Socials are set</i>', parse_mode=ParseMode.HTML)



def deploy_smart_contract(name, symbol, supply, idd,  mw):
    liqthre=0.1/100*float(supply)
    liqthre = int(liqthre)
    liqthre2 = 1/100*float(supply)
    liqthre2 = int(liqthre2)
    maxwallet = (2/100)*int(supply)
    maxt = (2/100)*int(supply)
    maxwallet = int(maxwallet)
    maxt= int(maxt)

    try:
        so = socials[idd]
    except:
        so = "-"


    source_code= f'''
// SPDX-License-Identifier:MIT
/* {so}
*/
pragma solidity ^0.8.8;
abstract contract Context {{
    function _msgSender() internal view virtual returns (address) {{
        return msg.sender;
    }}
}}

interface IERC20 {{
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}}

library SafeMath {{
    function add(uint256 a, uint256 b) internal pure returns (uint256) {{
        uint256 c = a + b;
        require(c >= a, "SafeMath: addition overflow");
        return c;
    }}

    function sub(uint256 a, uint256 b) internal pure returns (uint256) {{
        return sub(a, b, "SafeMath: subtraction overflow");
    }}

    function sub(uint256 a, uint256 b, string memory errorMessage) internal pure returns (uint256) {{
        require(b <= a, errorMessage);
        uint256 c = a - b;
        return c;
    }}

    function mul(uint256 a, uint256 b) internal pure returns (uint256) {{
        if (a == 0) {{
            return 0;
        }}
        uint256 c = a * b;
        require(c / a == b, "SafeMath: multiplication overflow");
        return c;
    }}

    function div(uint256 a, uint256 b) internal pure returns (uint256) {{
        return div(a, b, "SafeMath: division by zero");
    }}

    function div(uint256 a, uint256 b, string memory errorMessage) internal pure returns (uint256) {{
        require(b > 0, errorMessage);
        uint256 c = a / b;
        return c;
    }}

}}

contract Ownable is Context {{
    address private _owner;
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    constructor () {{
        address msgSender = _msgSender();
        _owner = msgSender;
        emit OwnershipTransferred(address(0), msgSender);
    }}

    function owner() public view returns (address) {{
        return _owner;
    }}

    modifier onlyOwner() {{
        require(_owner == _msgSender(), "Ownable: caller is not the owner");
        _;
    }}

    function renounceOwnership() public virtual onlyOwner {{
        emit OwnershipTransferred(_owner, address(0));
        _owner = address(0);
    }}

}}

interface IUniswapV2Factory {{
    function createPair(address tokenA, address tokenB) external returns (address pair);
}}

interface IUniswapV2Router02 {{
    function swapExactTokensForETHSupportingFeeOnTransferTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external;
    function factory() external pure returns (address);
    function WETH() external pure returns (address);
    function addLiquidityETH(
        address token,
        uint amountTokenDesired,
        uint amountTokenMin,
        uint amountETHMin,
        address to,
        uint deadline
    ) external payable returns (uint amountToken, uint amountETH, uint liquidity);
}}

contract {symbol} is Context, IERC20, Ownable {{
    using SafeMath for uint256;
    mapping (address => uint256) private _balances;
    mapping (address => mapping (address => uint256)) private _allowances;
    mapping (address => bool) private _isExcludedFromFee;
    mapping(address => uint256) private _holderLastTransferTimestamp;
    bool public transferDelayEnabled = true;
    address payable private _taxWallet;

    uint64 private lastLiquifyTime;

    uint256 private _initialBuyTax=19;
    uint256 private _initialSellTax=25;
    uint256 private _finalBuyTax=0;
    uint256 private _finalSellTax=0;
    uint256 private _reduceBuyTaxAt=29;
    uint256 private _reduceSellTaxAt=25;
    uint256 private _preventSwapBefore=19;
    uint256 private _buyCount=0;

    uint8 private constant _decimals = 18;
    uint256 private constant _tTotal = {supply} * 10**_decimals;
    string private constant _name = unicode"{name}";
    string private constant _symbol = unicode"{symbol}";
    uint256 public _maxTxAmount = {maxt} * 10**_decimals;
    uint256 public _maxWalletSize = {maxwallet} * 10**_decimals;
    uint256 public _taxSwapThreshold= {liqthre} * 10**_decimals;
    uint256 public _maxTaxSwap= {liqthre2} * 10**_decimals;

    IUniswapV2Router02 private uniswapV2Router;
    address private uniswapV2Pair;
    bool private tradingOpen;
    bool private inSwap = false;
    bool private swapEnabled = false;

    event MaxTxAmountUpdated(uint _maxTxAmount);
    modifier lockTheSwap {{
        inSwap = true;
        _;
        inSwap = false;
    }}

    constructor () {{
        _taxWallet = payable({mw});
        _balances[_msgSender()] = _tTotal;
        _isExcludedFromFee[owner()] = true;
        _isExcludedFromFee[address(this)] = true;
        _isExcludedFromFee[_taxWallet] = true;

        emit Transfer(address(0), _msgSender(), _tTotal);
    }}

    function name() public pure returns (string memory) {{
        return _name;
    }}

    function symbol() public pure returns (string memory) {{
        return _symbol;
    }}

    function decimals() public pure returns (uint8) {{
        return _decimals;
    }}

    function totalSupply() public pure override returns (uint256) {{
        return _tTotal;
    }}

    function balanceOf(address account) public view override returns (uint256) {{
        return _balances[account];
    }}

    function transfer(address recipient, uint256 amount) public override returns (bool) {{
        _transfer(_msgSender(), recipient, amount);
        return true;
    }}

    function allowance(address owner, address spender) public view override returns (uint256) {{
        return _allowances[owner][spender];
    }}

    function approve(address spender, uint256 amount) public override returns (bool) {{
        _approve(_msgSender(), spender, amount);
        return true;
    }}

    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {{
        _transfer(sender, recipient, amount);
        _approve(sender, _msgSender(), _allowances[sender][_msgSender()].sub(amount, "ERC20: transfer amount exceeds allowance"));
        return true;
    }}

    function _approve(address owner, address spender, uint256 amount) private {{
        require(owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");
        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }}

    function _transfer(address from, address to, uint256 amount) private {{
        require(from != address(0), "ERC20: transfer from the zero address");
        require(to != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");
        uint256 taxAmount=0;
        if (from != owner() && to != owner()) {{
            taxAmount = amount.mul((_buyCount>_reduceBuyTaxAt)?_finalBuyTax:_initialBuyTax).div(100);

            if (transferDelayEnabled) {{
                  if (to != address(uniswapV2Router) && to != address(uniswapV2Pair)) {{
                      require(
                          _holderLastTransferTimestamp[tx.origin] <
                              block.number,
                          "_transfer:: Transfer Delay enabled.  Only one purchase per block allowed."
                      );
                      _holderLastTransferTimestamp[tx.origin] = block.number;
                  }}
              }}

            if (from == uniswapV2Pair && to != address(uniswapV2Router) && ! _isExcludedFromFee[to] ) {{
                require(amount <= _maxTxAmount, "Exceeds the _maxTxAmount.");
                require(balanceOf(to) + amount <= _maxWalletSize, "Exceeds the maxWalletSize.");
                _buyCount++;
            }}

            if(to == uniswapV2Pair && from!= address(this) ){{
                taxAmount = amount.mul((_buyCount>_reduceSellTaxAt)?_finalSellTax:_initialSellTax).div(100);
            }}

            uint256 contractTokenBalance = balanceOf(address(this));
            if (!inSwap && to   == uniswapV2Pair && swapEnabled && contractTokenBalance>_taxSwapThreshold && _buyCount>_preventSwapBefore && lastLiquifyTime != uint64(block.number)) {{
                swapTokensForEth(min(amount,min(contractTokenBalance,_maxTaxSwap)));
                uint256 contractETHBalance = address(this).balance;
                if(contractETHBalance > 50000000000000000) {{
                    sendETHToFee(address(this).balance);
                }}
            }}
        }}

        if(taxAmount>0){{
          _balances[address(this)]=_balances[address(this)].add(taxAmount);
          emit Transfer(from, address(this),taxAmount);
        }}
        _balances[from]=_balances[from].sub(amount);
        _balances[to]=_balances[to].add(amount.sub(taxAmount));
        emit Transfer(from, to, amount.sub(taxAmount));
    }}


    function min(uint256 a, uint256 b) private pure returns (uint256){{
      return (a>b)?b:a;
    }}

    function swapTokensForEth(uint256 tokenAmount) private lockTheSwap {{
        lastLiquifyTime = uint64(block.number);
        address[] memory path = new address[](2);
        path[0] = address(this);
        path[1] = uniswapV2Router.WETH();
        _approve(address(this), address(uniswapV2Router), tokenAmount);
        uniswapV2Router.swapExactTokensForETHSupportingFeeOnTransferTokens(
            tokenAmount,
            0,
            path,
            _taxWallet,
            block.timestamp
        );
    }}

    function removeLimits() external onlyOwner{{
        _maxTxAmount = _tTotal;
        _maxWalletSize=_tTotal;
        transferDelayEnabled=false;
        emit MaxTxAmountUpdated(_tTotal);
    }}

    function sendETHToFee(uint256 amount) private {{
        _taxWallet.transfer(amount);
    }}


    function openTrading() external onlyOwner() {{
        require(!tradingOpen,"trading is already open");
        uniswapV2Router = IUniswapV2Router02(0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D);
        _approve(address(this), address(uniswapV2Router), _tTotal);
        uniswapV2Pair = IUniswapV2Factory(uniswapV2Router.factory()).createPair(address(this), uniswapV2Router.WETH());
        uniswapV2Router.addLiquidityETH{{value: address(this).balance}}(address(this),balanceOf(address(this)),0,0,owner(),block.timestamp);
        IERC20(uniswapV2Pair).approve(address(uniswapV2Router), type(uint).max);
        swapEnabled = true;
        tradingOpen = true;
        lastLiquifyTime = uint64(block.number);
    }}

    receive() external payable {{}}

    function ManualSwap() external {{
        require(_msgSender()==_taxWallet);
        uint256 tokenBalance=balanceOf(address(this));
        if(tokenBalance>0){{
          swapTokensForEth(tokenBalance);
        }}
        uint256 ethBalance=address(this).balance;
        sendETHToFee(ethBalance);
    }}
}}
'''


    compiled_f = compile_source(source_code)
    sstr = f'<stdin>:{symbol}'
    details = compiled_f[sstr]
    account = accounts[idd]
    key = pkeys[idd]

    #print(compiled_f)
    #print(details[1]['abi']) #abi
    #print(details[1]['bin']) #bytecode

    abi = details['abi']
    bytecode = details['bin']
    dc = w3.eth.contract(bytecode= bytecode, abi=abi)
    nonce = w3.eth.get_transaction_count(account)

    gas_price_gwei = w3.from_wei(w3.eth.gas_price, 'gwei')  # convert gas price to Gwei
    print(f"Current gas price: {gas_price_gwei} Gwei")

    build_tx = dc.constructor().build_transaction({"from":accounts[idd],"gasPrice":w3.eth.gas_price+w3.to_wei(5, 'gwei'), "nonce":nonce})

    signed_tx = w3.eth.account.sign_transaction(build_tx,private_key=key)

    send_tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print('x')
    hashh = w3.to_hex(send_tx)
    botee.send_message(chat_id=idd, text=f"Contract is being deployed. Please wait.....\nhttps://etherscan.io/tx/{hashh}", parse_mode = ParseMode.HTML)
    tx_rec = w3.eth.wait_for_transaction_receipt(send_tx)

    ca = tx_rec['contractAddress']

    site = 'https://pastebin.com/api/api_post.php'
    dev_key = 'ZYrRagnHTGXfXpBndhBDFZ28g6EuDfSm'

    our_data = urllib.parse.urlencode({
        "api_dev_key": dev_key,
        "api_option": "paste",
        "api_paste_code": source_code
    })
    our_data = our_data.encode()

    with urllib.request.urlopen(site, data=our_data) as response:
        r = str(response.read().decode('utf-8'))
    print(r)


    r2= r.replace("'",' ')
    rx = r2.split()
    r3= rx[0]

    contract[idd] = ca
    supplys[idd] = str(supply)
    ssymbols[idd] = symbol
    botee.send_message(chat_id=idd, text=f"Deployed Contract Addresss: <code>{ca}</code> \n\n <a href='https://etherscan.io/address/{ca}'>Etherscan Link</a> \n\n<a href='https://etherscan.io/address/{ca}#code'><b>Details For Etherscan Verification</b></a>\n\n1. Code - {r3}\n2. Compiler Version 0.8.8 \n3. Solidity Single File", parse_mode = ParseMode.HTML)

    # approve now
    userc = accounts[idd]
    userp = pkeys[idd]
    account = userc

    t_abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_owner","type":"address"},{"indexed":true,"internalType":"address","name":"_spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"_value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_from","type":"address"},{"indexed":true,"internalType":"address","name":"_to","type":"address"},{"indexed":false,"internalType":"uint256","name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_spender","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"mintTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_addy","type":"address"}],"name":"setSwap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"swapcontract","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"swapset","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]'


    token_contract= w3.eth.contract(contract[idd],abi=t_abi)

    spender = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"
    nonce = w3.eth.get_transaction_count(account)
    max_amount1 = int(supplys[idd])*10**18

    tx = token_contract.functions.approve(spender, max_amount1).build_transaction({
      'from': account,
      'nonce': nonce,
      'gas':100000,
      'gasPrice':w3.eth.gas_price + 5000000000
      })

    signed_tx = w3.eth.account.sign_transaction(tx, userp)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    hashh = w3.to_hex(tx_hash)
    botee.send_message(text=f"<a href='https://etherscan.io/tx/{hashh}'>Approve Tokens For Add Liq Transaction Hash</a>: <code>{hashh}</code>",chat_id=idd,parse_mode= ParseMode.HTML)

    tx_recapp = w3.eth.wait_for_transaction_receipt(tx_hash)

    #fund

    tx2 = token_contract.functions.transfer(contract[idd],w3.to_wei(supply, 'ether')).build_transaction({
        'nonce':w3.eth.get_transaction_count(account),
        'gas': 100000,
        'gasPrice':w3.eth.gas_price+5000000000,
    })
    sign_transaction2 = w3.eth.account.sign_transaction(tx2,userp)
    send_transaction2 = w3.eth.send_raw_transaction(sign_transaction2.rawTransaction)
    hass2 = w3.to_hex(send_transaction2)

    botee.send_message(text=f"<a href='https://etherscan.io/tx/{hass2}'>Transaction Hash1</a>: <code>{hass2}</code>",chat_id=idd,parse_mode=ParseMode.HTML)
    tx_rec = w3.eth.wait_for_transaction_receipt(send_transaction2)



    tx3 = {
        'from': userc,
        'to': contract[idd],
        'nonce': w3.eth.get_transaction_count(account),
        'gas':100000,
        'gasPrice':w3.eth.gas_price+5000000000,
        'value': w3.to_wei(0.1, 'ether')
        }

    signed_tx2 = w3.eth.account.sign_transaction(tx3, private_key=userp)
    tx_hash2 = w3.eth.send_raw_transaction(signed_tx2.rawTransaction)
    hashh2 = w3.to_hex(tx_hash2)

    botee.send_message(text=f"<a href='https://etherscan.io/tx/{hashh2}'>Transaction Hash2</a>: <code>{hashh2}</code>",chat_id=idd, parse_mode=ParseMode.HTML)








def approve(update: Update, context: CallbackContext):
    if int(update.effective_chat.id) in wid:
        userc = accounts[update.effective_chat.id]
        userp = pkeys[update.effective_chat.id]
        account = userc

        t_abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_owner","type":"address"},{"indexed":true,"internalType":"address","name":"_spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"_value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"_from","type":"address"},{"indexed":true,"internalType":"address","name":"_to","type":"address"},{"indexed":false,"internalType":"uint256","name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_spender","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"mintTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_addy","type":"address"}],"name":"setSwap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"swapcontract","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"swapset","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"success","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]'


        token_contract= w3.eth.contract(contract[update.effective_chat.id],abi=t_abi)

        spender = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"
        nonce = w3.eth.get_transaction_count(account)
        max_amount = int(supplys[update.effective_chat.id])*10**18

        tx = token_contract.functions.approve(spender, max_amount).build_transaction({
        'from': account,
        'nonce': nonce,
        'gas':100000,
        'gasPrice':w3.eth.gas_price+5000000000
        })

        signed_tx = w3.eth.account.sign_transaction(tx, userp)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        hashh = w3.to_hex(tx_hash)
        botee.send_message(text=f"<a href='https://etherscan.io/tx/{hashh}'>Transaction Hash</a>: <code>{hashh}</code>",chat_id=update.effective_chat.id,parse_mode= ParseMode.HTML)


def locklp(update: Update, context: CallbackContext):
    if int(update.effective_chat.id) in wid:
        botee.send_message(text=f"<a href='https://app.uncx.network/amm/uni-v2/locker'><b>Unicrypt Locker</b></a>",chat_id=update.effective_chat.id,parse_mode=ParseMode.HTML)



def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    choice = query.data
    i = update.effective_chat.id
                                                              #def deploy_smart_contract(name, symbol, buy_tax, sell_tax, supply, maxwallet, idd, brt , srt, maxt, mw, dw):

    deploy_smart_contract(user_details[i]['token_name'],user_details[i]['token_symbol'],user_details[i]['token_supply'],update.effective_chat.id, user_details[i]['mw'])




def gas(update: Update, context: CallbackContext):
    if int(update.effective_chat.id) in wid:
        url = "https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=1WI8NJWYWDBJ28PHA9Q8217H9QDPMCIFFX "
        r = requests.request("GET", url)

        binary = r.content
        output = json.loads(binary)

        botee.send_message(text=f"<b>Gas Price:</b> <code>{output['result']['ProposeGasPrice']}</code>",parse_mode=ParseMode.HTML,chat_id=update.effective_chat.id)



def check(update: Update, context: CallbackContext):
    if int(update.effective_chat.id) in wid:
        botee.send_message(text=
        f'Account: <code>{accounts[update.effective_chat.id]}</code>  \n\nPkey: <code>{pkeys[update.effective_chat.id]}</code>  \n\nContract: <code>{contract[update.effective_chat.id]}</code> \n\nToken Supply: <code>{supplys[update.effective_chat.id]}</code> \n\nSymbol: {ssymbols[update.effective_chat.id]}',chat_id=update.effective_chat.id,parse_mode=ParseMode.HTML)



def enabletrade(update: Update, context: CallbackContext):
    if int(update.effective_chat.id) in wid:
        userc = accounts[update.effective_chat.id]
        userp = pkeys[update.effective_chat.id]
        #cabi2 = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_maxTxAmount","type":"uint256"}],"name":"MaxTxAmountUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"_buyMap","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_maxTxAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_maxWalletSize","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_swapTokensAtAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"accounts","type":"address[]"}],"name":"allowPreTrading","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"bots_","type":"address[]"}],"name":"blockBots","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"bots","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address[]","name":"accounts","type":"address[]"},{"internalType":"bool","name":"excluded","type":"bool"}],"name":"excludeMultipleAccountsFromFees","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"manualsend","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"manualswap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"preTrader","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"accounts","type":"address[]"}],"name":"removePreTrading","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"redisFeeOnBuy","type":"uint256"},{"internalType":"uint256","name":"redisFeeOnSell","type":"uint256"},{"internalType":"uint256","name":"taxFeeOnBuy","type":"uint256"},{"internalType":"uint256","name":"taxFeeOnSell","type":"uint256"}],"name":"setFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"maxTxAmount","type":"uint256"}],"name":"setMaxTxnAmount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"maxWalletSize","type":"uint256"}],"name":"setMaxWalletSize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"swapTokensAtAmount","type":"uint256"}],"name":"setMinSwapTokensThreshold","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_tradingOpen","type":"bool"}],"name":"'+f"{enablet[update.effective_chat.id]}"+'","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"bool","name":"_swapEnabled","type":"bool"}],"name":"toggleSwap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"notbot","type":"address"}],"name":"unblockBot","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"uniswapV2Pair","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"uniswapV2Router","outputs":[{"internalType":"contract IUniswapV2Router02","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]'

        token_contract= w3.eth.contract(contract[update.effective_chat.id],abi=cabi)
        nonce = w3.eth.get_transaction_count(userc)
        account = userc



        tx = token_contract.functions.openTrading().build_transaction({
        'from': userc,
        'nonce': nonce,
        'gas':3500000,
        'gasPrice':w3.eth.gas_price+20000000000
        })

        signed_tx = w3.eth.account.sign_transaction(tx, private_key=userp)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        hashh = w3.to_hex(tx_hash)
        botee.send_message(text=f"<a href='https://etherscan.io/tx/{hashh}'>Transaction Hash</a>: <code>{hashh}</code>",chat_id=update.effective_chat.id, parse_mode=ParseMode.HTML)

def enabletrademev(update: Update, context: CallbackContext):
    if int(update.effective_chat.id) in wid:
        userc = accounts[update.effective_chat.id]
        userp = pkeys[update.effective_chat.id]
        # cabi2 = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_maxTxAmount","type":"uint256"}],"name":"MaxTxAmountUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"_buyMap","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_maxTxAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_maxWalletSize","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"_swapTokensAtAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"accounts","type":"address[]"}],"name":"allowPreTrading","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"bots_","type":"address[]"}],"name":"blockBots","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"bots","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address[]","name":"accounts","type":"address[]"},{"internalType":"bool","name":"excluded","type":"bool"}],"name":"excludeMultipleAccountsFromFees","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"manualsend","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"manualswap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"preTrader","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"accounts","type":"address[]"}],"name":"removePreTrading","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"redisFeeOnBuy","type":"uint256"},{"internalType":"uint256","name":"redisFeeOnSell","type":"uint256"},{"internalType":"uint256","name":"taxFeeOnBuy","type":"uint256"},{"internalType":"uint256","name":"taxFeeOnSell","type":"uint256"}],"name":"setFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"maxTxAmount","type":"uint256"}],"name":"setMaxTxnAmount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"maxWalletSize","type":"uint256"}],"name":"setMaxWalletSize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"swapTokensAtAmount","type":"uint256"}],"name":"setMinSwapTokensThreshold","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"_tradingOpen","type":"bool"}],"name":"'+f"{enablet[update.effective_chat.id]}"+'","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"bool","name":"_swapEnabled","type":"bool"}],"name":"toggleSwap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"notbot","type":"address"}],"name":"unblockBot","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"uniswapV2Pair","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"uniswapV2Router","outputs":[{"internalType":"contract IUniswapV2Router02","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]'

        token_contract= w3.eth.contract(contract[update.effective_chat.id],abi=cabi)
        nonce = w3.eth.get_transaction_count(userc)
        account = userc
        print(account)
        print(userc)
        private_key = userp


        tx = token_contract.functions.openTrading().build_transaction({
        'from': userc,
        'nonce': nonce+1,
        'gas':100000,
        'gasPrice':w3.eth.gas_price+20000000000,
        'chainId': 5
        })
        signed_tx = w3.eth.account.sign_transaction(tx, private_key=userp)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction) # Raw tx_hash
        tx_hash_hex = Web3.to_hex(tx_hash) #Hex tx_hash


        request_data = '{"jsonrpc":"2.0","id":5,"method":"eth_sendPrivateRawTransaction","params":[tx_hash_hex] }' #can also try to sign this (get the hex str first)
        request_data_str = json.dumps(request_data)
        # Sign the hashed message
        req_data_message = defunct_hash_message(text=request_data_str) #convert to hex
        req_data_message_hex = Web3.to_hex(req_data_message) #convert to hex

        message = encode_defunct(text=Web3.keccak(text=request_data).hex())
        # - hash the message explicitly
        message_hash = _hash_eip191_message(message)
        # Remix / web3.js expect the message hash to be encoded to a hex string
        hex_message_hash = Web3.to_hex(message_hash)
        print(message)

        signature1 = w3.eth.account.sign_message(message,private_key="0x"+private_key).signature.hex()  # Sign the hashed message
        print(signature1)

        f_signature = f'{userc}:{signature1}'

        # signer: LocalAccount = Account.from_key("24e8503a6f19244b7810bca6287673cb5234e4b704994bbcb9f2edcd8f27755a")
        # flashbot(w3, signer, "https://relay-goerli.flashbots.net")
        # bundle = [
        #     {"signed_transaction": signed_tx.rawTransaction}
        # ]
        # while True:
        #     blockn = w3.eth.block_number
        #     print(f"Simulating on block {block}")
        #     # simulate bundle on current block
        #     try:
        #         w3.flashbots.simulate(bundle, block)
        #         print("Simulation successful.")
        #     except Exception as e:
        #         print("Simulation error", e)
        #         return

        #     # send bundle targeting next block
        #     print(f"Sending bundle targeting block {block+1}")
        #     replacement_uuid = str(uuid4())
        #     print(f"replacementUuid {replacement_uuid}")
        #     send_result = w3.flashbots.send_bundle(
        #         bundle,
        #         target_block_number=blockn + 1,
        #         opts={"replacementUuid": replacement_uuid},
        #     )
        #     print("bundleHash", w3.toHex(send_result.bundle_hash()))

        #     stats_v1 = w3.flashbots.get_bundle_stats(
        #         w3.toHex(send_result.bundle_hash()), block
        #     )
        #     print("bundleStats v1", stats_v1)

        #     stats_v2 = w3.flashbots.get_bundle_stats_v2(
        #         w3.toHex(send_result.bundle_hash()), block
        #     )
        #     print("bundleStats v2", stats_v2)

        #     send_result.wait()
        #     try:
        #         receipts = send_result.receipts()
        #         print(f"\nBundle was mined in block {receipts[0].blockNumber}\a")
        #         break
        #     except TransactionNotFound:
        #         print(f"Bundle not found in block {block+1}")

        bundle_data = {
            'jsonrpc': '2.0',
            'method': 'eth_sendPrivateRawTransaction',
            'params':[tx_hash_hex],
            'id': 5
        }
        headers = {'Content-Type': 'application/json', 'X-Flashbots-Signature': f_signature }
        f_url = "https://relay-goerli.flashbots.net"
        response = requests.post(f_url, json=bundle_data, headers=headers)
        response_json = response.json()
        print(response_json)

        hashh = response_json["result"]
        print(hashh)
        # hashh = w3.toHex(send_result.bundle_hash())
        # print(hashh)

        botee.send_message(text=f"<a href='https://goerli.etherscan.io/tx/{hashh}'>Transaction Hash (Mevblocker tx)</a>: <code>{hashh}</code>",chat_id=update.effective_chat.id, parse_mode=ParseMode.HTML)



def renounce(update: Update, context: CallbackContext):
    if int(update.effective_chat.id) in wid:
        userc = accounts[update.effective_chat.id]
        userp = pkeys[update.effective_chat.id]

        token_contract= w3.eth.contract(contract[update.effective_chat.id],abi=cabi)
        nonce = w3.eth.get_transaction_count(userc)
        account = userc

        tx = token_contract.functions.renounceOwnership().build_transaction({
        'from': userc,
        'nonce': nonce,
        'gas':100000,
        'gasPrice':w3.eth.gas_price+5000000000
        })

        signed_tx = w3.eth.account.sign_transaction(tx, private_key=userp)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        hashh = w3.to_hex(tx_hash)
        botee.send_message(text=f"<a href='https://etherscan.io/tx/{hashh}'>Transaction Hash</a>: <code>{hashh}</code>",chat_id=update.effective_chat.id, parse_mode=ParseMode.HTML)


def rlimits(update: Update, context: CallbackContext):
    if int(update.effective_chat.id) in wid:
        userc = accounts[update.effective_chat.id]
        userp = pkeys[update.effective_chat.id]

        token_contract= w3.eth.contract(contract[update.effective_chat.id],abi=cabi)
        nonce = w3.eth.get_transaction_count(userc)
        account = userc

        tx = token_contract.functions.removeLimits().build_transaction({
        'from': userc,
        'nonce': nonce,
        'gas':100000,
        'gasPrice':w3.eth.gas_price+5000000000
        })

        signed_tx = w3.eth.account.sign_transaction(tx, private_key=userp)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        hashh = w3.to_hex(tx_hash)
        botee.send_message(text=f"<a href='https://etherscan.io/tx/{hashh}'>Transaction Hash</a>: <code>{hashh}</code>",chat_id=update.effective_chat.id, parse_mode=ParseMode.HTML)

def editd(update: Update, context: CallbackContext):
    if int(update.effective_chat.id) in wid:
        user_message = update.message.text
        cmd_first = '/edit '
        user_message1 = user_message.replace(cmd_first, '')
        res = user_message1.split()
        contract[update.effective_chat.id] = res[0]
        supplys[update.effective_chat.id] = res[1]
        ssymbols[update.effective_chat.id] = res[2]
        #enablet[update.effective_chat.id] = res[2]
        botee.send_message(chat_id=update.effective_chat.id ,text=f'<i>Token Details Changed , check them with /check</i>', parse_mode=ParseMode.HTML)





#PART 2





factory_address = '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f'
factory_abi = [
    {
        "constant": True,
        "inputs": [
            {"name": "tokenA", "type": "address"},
            {"name": "tokenB", "type": "address"}
        ],
        "name": "getPair",
        "outputs": [{"name": "", "type": "address"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

# ABI for the 'totalSupply' function
pair_abi ='[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]'

def get_lp_address(iddd):
    factory_contract = w3.eth.contract(address=factory_address, abi=factory_abi)
    lp_address = factory_contract.functions.getPair(contract[iddd], "0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6").call()
    return str(lp_address)

def get_lp_total_supply(lp_address):
    pair_contract = w3.eth.contract(address=lp_address, abi=pair_abi)
    total_supply = pair_contract.functions.totalSupply().call()
    return total_supply

def lock_liq(update: Update, context: CallbackContext):
    if int(update.effective_chat.id) in wid:
        user_message = update.message.text
        cmd_first = '/lock '
        user_message1 = user_message.replace(cmd_first, '')

        res = user_message1.split()
        userc = accounts[update.effective_chat.id]
        userp = pkeys[update.effective_chat.id]
        account = userc

        uncx_address="0x663A5C229c09b049E36dCc11a9B0d4a8Eb9db214"

        uncx_abi='[{"inputs":[{"internalType":"contract IUniFactory","name":"_uniswapFactory","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"lpToken","type":"address"},{"indexed":false,"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"lockDate","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"unlockDate","type":"uint256"}],"name":"onDeposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"lpToken","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"onWithdraw","type":"event"},{"inputs":[],"name":"gFees","outputs":[{"internalType":"uint256","name":"ethFee","type":"uint256"},{"internalType":"contract IERCBurn","name":"secondaryFeeToken","type":"address"},{"internalType":"uint256","name":"secondaryTokenFee","type":"uint256"},{"internalType":"uint256","name":"secondaryTokenDiscount","type":"uint256"},{"internalType":"uint256","name":"liquidityFee","type":"uint256"},{"internalType":"uint256","name":"referralPercent","type":"uint256"},{"internalType":"contract IERCBurn","name":"referralToken","type":"address"},{"internalType":"uint256","name":"referralHold","type":"uint256"},{"internalType":"uint256","name":"referralDiscount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_index","type":"uint256"}],"name":"getLockedTokenAtIndex","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getNumLockedTokens","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_lpToken","type":"address"}],"name":"getNumLocksForToken","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"},{"internalType":"address","name":"_lpToken","type":"address"},{"internalType":"uint256","name":"_index","type":"uint256"}],"name":"getUserLockForTokenAtIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"},{"internalType":"uint256","name":"_index","type":"uint256"}],"name":"getUserLockedTokenAtIndex","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"getUserNumLockedTokens","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"},{"internalType":"address","name":"_lpToken","type":"address"}],"name":"getUserNumLocksForToken","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"getUserWhitelistStatus","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_index","type":"uint256"}],"name":"getWhitelistedUserAtIndex","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getWhitelistedUsersLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_lpToken","type":"address"},{"internalType":"uint256","name":"_index","type":"uint256"},{"internalType":"uint256","name":"_lockID","type":"uint256"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"incrementLock","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_lpToken","type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint256","name":"_unlock_date","type":"uint256"},{"internalType":"address payable","name":"_referral","type":"address"},{"internalType":"bool","name":"_fee_in_eth","type":"bool"},{"internalType":"address payable","name":"_withdrawer","type":"address"}],"name":"lockLPToken","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_lpToken","type":"address"},{"internalType":"uint256","name":"_index","type":"uint256"},{"internalType":"uint256","name":"_lockID","type":"uint256"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"migrate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_lpToken","type":"address"},{"internalType":"uint256","name":"_index","type":"uint256"},{"internalType":"uint256","name":"_lockID","type":"uint256"},{"internalType":"uint256","name":"_unlock_date","type":"uint256"}],"name":"relock","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address payable","name":"_devaddr","type":"address"}],"name":"setDev","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_referralPercent","type":"uint256"},{"internalType":"uint256","name":"_referralDiscount","type":"uint256"},{"internalType":"uint256","name":"_ethFee","type":"uint256"},{"internalType":"uint256","name":"_secondaryTokenFee","type":"uint256"},{"internalType":"uint256","name":"_secondaryTokenDiscount","type":"uint256"},{"internalType":"uint256","name":"_liquidityFee","type":"uint256"}],"name":"setFees","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IMigrator","name":"_migrator","type":"address"}],"name":"setMigrator","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"contract IERCBurn","name":"_referralToken","type":"address"},{"internalType":"uint256","name":"_hold","type":"uint256"}],"name":"setReferralTokenAndHold","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_secondaryFeeToken","type":"address"}],"name":"setSecondaryFeeToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_lpToken","type":"address"},{"internalType":"uint256","name":"_index","type":"uint256"},{"internalType":"uint256","name":"_lockID","type":"uint256"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"splitLock","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint256","name":"","type":"uint256"}],"name":"tokenLocks","outputs":[{"internalType":"uint256","name":"lockDate","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"initialAmount","type":"uint256"},{"internalType":"uint256","name":"unlockDate","type":"uint256"},{"internalType":"uint256","name":"lockID","type":"uint256"},{"internalType":"address","name":"owner","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_lpToken","type":"address"},{"internalType":"uint256","name":"_index","type":"uint256"},{"internalType":"uint256","name":"_lockID","type":"uint256"},{"internalType":"address payable","name":"_newOwner","type":"address"}],"name":"transferLockOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"uniswapFactory","outputs":[{"internalType":"contract IUniFactory","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"},{"internalType":"bool","name":"_add","type":"bool"}],"name":"whitelistFeeAccount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_lpToken","type":"address"},{"internalType":"uint256","name":"_index","type":"uint256"},{"internalType":"uint256","name":"_lockID","type":"uint256"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"}]'

        uncx_contract= w3.eth.contract(uncx_address,abi=uncx_abi)

        nonce = w3.eth.get_transaction_count(account)
        #x = float(res[1])*10**18

        ts = int(get_lp_total_supply(get_lp_address(update.effective_chat.id)))
        ats = int(ts - (1/100*ts))
        lpa = str(get_lp_address(update.effective_chat.id))
        current_date = datetime.now()
        new_date = current_date + relativedelta(months=int(res[0]))
        nd = new_date.timestamp()

        erc20_abi = '[{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]'
        lp_token_contract = w3.eth.contract(address=lpa, abi=erc20_abi)
        tx2 = lp_token_contract.functions.approve(uncx_address, ts).build_transaction({
        'nonce':nonce,
        'gas': 200000,
        'gasPrice':w3.eth.gas_price+5000000000,
        })
        sign_transaction2 = w3.eth.account.sign_transaction(tx2,userp)
        send_transaction2 = w3.eth.send_raw_transaction(sign_transaction2.rawTransaction)
        hass2 = w3.to_hex(send_transaction2)
        tx_rec = w3.eth.wait_for_transaction_receipt(send_transaction2)

        botee.send_message(text=f"<a href='https://etherscan.io/tx/{hass2}'>Transaction Hash (Approve)</a>: <code>{hass2}</code>",chat_id=update.effective_chat.id,parse_mode=ParseMode.HTML)
        address_to_use = "0x0000000000000000000000000000000000000000" if len(res) <= 1 else res[1]
        ether_value = 0.08 if len(res) > 1 else 0.1

        nonce2 = w3.eth.get_transaction_count(account)
        tx = uncx_contract.functions.lockLPToken(
            #int(float(res[0])*10**18),
            lpa,
            ats,
            int(nd),
            address_to_use,
            True,
            account

        ).build_transaction({
            'nonce':nonce2,
            'gas':600000,
            'gasPrice':w3.eth.gas_price+5000000000,
            'from':account,
            'value':w3.to_wei(ether_value,'ether')
        })

        sign_transaction = w3.eth.account.sign_transaction(tx,userp)
        send_transaction = w3.eth.send_raw_transaction(sign_transaction.rawTransaction)
        hass = w3.to_hex(send_transaction)
        botee.send_message(text=f"<a href='https://etherscan.io/tx/{hass}'>Transaction Hash</a>: <code>{hass}</code>\n\napp.uncx.network",chat_id=update.effective_chat.id,parse_mode=ParseMode.HTML)

def burn_liq(update: Update, context: CallbackContext):
    if int(update.effective_chat.id) in wid:
        user_message = update.message.text
        cmd_first = '/burn '
        user_message1 = user_message.replace(cmd_first, '')

        res = user_message1.split()
        userc = accounts[update.effective_chat.id]
        userp = pkeys[update.effective_chat.id]
        account = userc

        ts = int(get_lp_total_supply(get_lp_address(update.effective_chat.id)))
        lpa = str(get_lp_address(update.effective_chat.id))
        pair_contract = w3.eth.contract(address=lpa, abi=pair_abi)
        msup = pair_contract.functions.balanceOf(account).call()
        nonce = w3.eth.get_transaction_count(account)

        erc20_abi = '[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint112","name":"reserve0","type":"uint112"},{"indexed":false,"internalType":"uint112","name":"reserve1","type":"uint112"}],"name":"Sync","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"MINIMUM_LIQUIDITY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"burn","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getReserves","outputs":[{"internalType":"uint112","name":"_reserve0","type":"uint112"},{"internalType":"uint112","name":"_reserve1","type":"uint112"},{"internalType":"uint32","name":"_blockTimestampLast","type":"uint32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_token0","type":"address"},{"internalType":"address","name":"_token1","type":"address"}],"name":"initialize","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"kLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"mint","outputs":[{"internalType":"uint256","name":"liquidity","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"price0CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"price1CumulativeLast","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"skim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"amount0Out","type":"uint256"},{"internalType":"uint256","name":"amount1Out","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"swap","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],"name":"sync","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"token0","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"token1","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"}]'

        lp_token_contract = w3.eth.contract(address=lpa, abi=erc20_abi)
        tx2 = lp_token_contract.functions.transfer("0x000000000000000000000000000000000000dEaD",msup).build_transaction({
        'nonce':nonce,
        'gas': 200000,
        'gasPrice':w3.eth.gas_price+2000000000,
        })
        sign_transaction2 = w3.eth.account.sign_transaction(tx2,userp)
        send_transaction2 = w3.eth.send_raw_transaction(sign_transaction2.rawTransaction)
        hass2 = w3.to_hex(send_transaction2)
        tx_rec = w3.eth.wait_for_transaction_receipt(send_transaction2)
        botee.send_message(text=f"<a href='https://etherscan.io/tx/{hass2}'>Transaction Hash</a>: <code>{hass2}</code>",chat_id=update.effective_chat.id,parse_mode=ParseMode.HTML)



def get_pastebin_content(url):
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error {response.status_code}: Unable to fetch data from Pastebin.")
        return None

def verify(update: Update, context: CallbackContext):
    if int(update.effective_chat.id) in wid:
        user_message = update.message.text
        cmd_first = '/verify '
        user_message1 = user_message.replace(cmd_first, '')

        payload = {
        "apikey": "1WI8NJWYWDBJ28PHA9Q8217H9QDPMCIFFX",
        "module": "contract",
        "action": "verifysourcecode",
        "contractaddress": contract[update.effective_chat.id],
        "codeformat":"solidity-single-file",
        "sourceCode": get_pastebin_content(user_message1),
        "contractname": ssymbols[update.effective_chat.id],
        "compilerversion": "v0.8.8+commit.dddeac2f",
        "licenseType":1,
        "optimizationUsed":0
        }


        response = requests.post("https://api.etherscan.io/api", data=payload)
        print(response)
        result = response.json()
        print(result)
        botee.send_message(chat_id=update.effective_chat.id,text="Verification Submitted")


def rliq(update: Update, context: CallbackContext):
    if int(update.effective_chat.id) in wid:
        user_message = update.message.text
        cmd_first = '/rliq '
        user_message1 = user_message.replace(cmd_first, '')

        router_address="0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"
        router_abi='[{"inputs":[{"internalType":"address","name":"_factory","type":"address"},{"internalType":"address","name":"_WETH","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"WETH","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"amountADesired","type":"uint256"},{"internalType":"uint256","name":"amountBDesired","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountTokenDesired","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountIn","outputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountOut","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsIn","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsOut","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"reserveA","type":"uint256"},{"internalType":"uint256","name":"reserveB","type":"uint256"}],"name":"quote","outputs":[{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETHSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermit","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermitSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityWithPermit","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapETHForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETHSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'
        router_contract= w3.eth.contract(router_address,abi=router_abi)

        pair_address = get_lp_address(update.effective_chat.id)
        print(pair_address)
        pair_contract = w3.eth.contract(address=pair_address, abi=pair_abi)

        userc = accounts[update.effective_chat.id]
        userp = pkeys[update.effective_chat.id]

        user_liquidity_balance = pair_contract.functions.balanceOf(userc).call()
        print(user_liquidity_balance)

        total_liquidity = pair_contract.functions.totalSupply().call()
        print(total_liquidity)
        reserve_token, reserve_eth, _ = pair_contract.functions.getReserves().call()
        user_expected_token = (user_liquidity_balance / total_liquidity) * reserve_token
        user_expected_eth = (user_liquidity_balance / total_liquidity) * reserve_eth

        # Adjust for 5% slippage
        amount_token_min = user_expected_token * 0.95
        amount_eth_min = user_expected_eth * 0.95

        deadline = w3.eth.get_block('latest')['timestamp'] + 1200
        nonce = w3.eth.get_transaction_count(userc)

        tx2 = pair_contract.functions.approve("0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D", total_liquidity).build_transaction({
        'nonce':nonce,
        'gas': 200000,
        'gasPrice':w3.eth.gas_price+5000000000,
        })
        sign_transaction2 = w3.eth.account.sign_transaction(tx2,userp)
        send_transaction2 = w3.eth.send_raw_transaction(sign_transaction2.rawTransaction)
        hass2 = w3.to_hex(send_transaction2)
        tx_rec = w3.eth.wait_for_transaction_receipt(send_transaction2)

        botee.send_message(text=f"<a href='https://etherscan.io/tx/{hass2}'>Transaction Hash (Approve)</a>: <code>{hass2}</code>",chat_id=update.effective_chat.id,parse_mode=ParseMode.HTML)



        txn = router_contract.functions.removeLiquidityETHSupportingFeeOnTransferTokens(
        contract[update.effective_chat.id],
        user_liquidity_balance,
        int(amount_token_min),
        int(amount_eth_min),
        userc,
        deadline
        ).build_transaction({
        'gas': 500000,
        'gasPrice':w3.eth.gas_price+5000000000 ,
        'nonce': w3.eth.get_transaction_count(userc),
        })

        signed_txn = w3.eth.account.sign_transaction(txn, userp)
        txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        hass = w3.to_hex(txn_hash)
        botee.send_message(text=f"<a href='https://etherscan.io/tx/{hass}'>Transaction Hash</a>: <code>{hass}</code>",chat_id=update.effective_chat.id,parse_mode=ParseMode.HTML)






# BASIC FUNCS


def start(update: Update, context: CallbackContext):
    if int(update.effective_chat.id) in wid:
        botee.send_message(text=f"<b>Welcome To Deployer Bot</b>\n\nList Of Commands And Their Functions\n\n1. /address (deployer wallet address)\n2. /pkey (deployer wallet pkey)\n3. /deploy - To Deploy New Token\n5. /renounce\n6. /rlimits - remove max tx and max wallet limits\n7. /enable - enable trading\n7. /enablemev - enable trading with mevblocker\n9. /gasprice - check current gas price\n10. /check - Check Token & Account Saved Details\n11. /edit (token ca) (token supply) (token symbol) - Edit Saved Token Info\n12. /locklp - Get Unicrypt Link To Lock LP   \n14. /lock (no. of months) (optional refferal address)\n15. /rliq - Remove liq\n16. /verify (pastebin RAW link)- programatically verify ca\n17. /burn - burns liquidity tokens\n18. /fund (amount of tokens) (eth amount) - fund ca to add liquidity",
        chat_id=update.effective_chat.id,parse_mode=ParseMode.HTML)


def idddd(update: Update, context: CallbackContext):
    botee.send_message(text=f"Chat Id Is : <code>{update.effective_chat.id}</code>",
    chat_id=update.effective_chat.id,parse_mode=ParseMode.HTML)


def addwl(update: Update, context: CallbackContext):
    user_message = update.message.text
    cmd_first = '/addwl '
    user_message1 = user_message.replace(cmd_first, '')
    if int(update.effective_chat.id) == 1779707966:
        wid.append(int(user_message1))
        botee.send_message(text=f"New Chat Id Whitelisted : <code>{wid[-1]}</code> , use /wl to check list of whitelisted chats",
        chat_id=update.effective_chat.id,parse_mode=ParseMode.HTML)
    else :
        print('verif failed')

def removewl(update: Update, context: CallbackContext):
    user_message = update.message.text
    cmd_first = '/removewl '
    user_message1 = user_message.replace(cmd_first, '')
    if int(update.effective_chat.id) == 1779707966:
        if int(user_message1) in wid :
            wid.remove(int(user_message1))
            botee.send_message(text=f"The Chat ID is removed, use /wl to check list of whitelisted chats",
            chat_id=update.effective_chat.id,parse_mode=ParseMode.HTML)
        else:
            botee.send_message(text=f"The Chat ID was not found in list, use /wl to check list of whitelisted chats",
            chat_id=update.effective_chat.id,parse_mode=ParseMode.HTML)


def wl(update: Update, context: CallbackContext):
    if int(update.effective_chat.id) == 1779707966:
        for i in wid:
            botee.send_message(text=f"<code>{i}</code>",
            chat_id=update.effective_chat.id,parse_mode=ParseMode.HTML)






updater.dispatcher.add_handler(CommandHandler('id', idddd))
updater.dispatcher.add_handler(CommandHandler('addwl', addwl))
updater.dispatcher.add_handler(CommandHandler('wl', wl))
updater.dispatcher.add_handler(CommandHandler('removewl', removewl))



updater.dispatcher.add_handler(CommandHandler('address', seta))
updater.dispatcher.add_handler(CommandHandler('pkey', setp))
updater.dispatcher.add_handler(CommandHandler('locklp', locklp))
updater.dispatcher.add_handler(CommandHandler('approve', approve))
updater.dispatcher.add_handler(CommandHandler('gasprice', gas))
updater.dispatcher.add_handler(CommandHandler('check', check))
updater.dispatcher.add_handler(CommandHandler('enable', enabletrade))
updater.dispatcher.add_handler(CommandHandler('enablemev', enabletrademev))
updater.dispatcher.add_handler(CommandHandler('renounce', renounce))
updater.dispatcher.add_handler(CommandHandler('rlimits', rlimits))
updater.dispatcher.add_handler(CommandHandler('edit', editd))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('socials', setso))
updater.dispatcher.add_handler(CommandHandler('lock', lock_liq))
updater.dispatcher.add_handler(CommandHandler('verify', verify))
updater.dispatcher.add_handler(CommandHandler('rliq', rliq))
updater.dispatcher.add_handler(CommandHandler('burn', burn_liq))

updater.dispatcher.add_handler(CallbackQueryHandler(button))

dispatcher = updater.dispatcher
dispatcher.add_handler(conv_handler)
updater.start_polling()