# -*- coding: utf-8 -*-
"""
MIT License

Copyright (c) 2020 gomashio1596

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

try:
    from typing import Optional, Union, Type, Any, List
    from threading import Thread, Timer
    from functools import partial
    import unicodedata
    import threading
    import traceback
    import datetime
    import asyncio
    import logging
    import random
    import time
    import sys
    import os
    import re
except ModuleNotFoundError as e:
    try:
        import traceback
        print(f'{traceback.format_exc()}')
    except ModuleNotFoundError:
        pass
    try:
        import sys
        print(f'Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}\n')
    except ModuleNotFoundError:
        pass
    print(e)
    print('標準ライブラリの読み込みに失敗しました。Pythonのバージョンが間違っている可能性があります。Pythonの再インストールなどを試してみてください。問題が修正されない場合はこちらまで連絡をください\nTwitter @gomashioepic\nDiscord gomashio#4335')
    print('Failed to load basic library. Python version maybe wrong. Try reinstall Python. If the issue is not resolved, please contact me\nTwitter @gomashioepic\nDiscord gomashio#4335')
    sys.exit(1)

try:
    from crayons import cyan, green, magenta, red, yellow
    from fortnitepy import ClientPartyMember
    from flask import Flask
    import fortnitepy.errors
    import fortnitepy
    import requests
    import discord
    import jaconv
    import json
except ModuleNotFoundError as e:
    try:
        import traceback
        print(f'{traceback.format_exc()}')
    except ModuleNotFoundError:
        pass
    try:
        import sys
        print(f'Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}\n')
    except ModuleNotFoundError:
        pass
    print(e)
    print('サードパーティーライブラリの読み込みに失敗しました。INSTALL.bat を実行してください。問題が修正されない場合はこちらまで連絡をください\nTwitter @gomashioepic\nDiscord gomashio#4335')
    print('Failed to load third party library. Please run INSTALL.bat. If the issue is not resolved, please contact me\nTwitter @gomashioepic\nDiscord gomashio#4335')
    sys.exit(1)

if os.getcwd().startswith('/app'):
    app=Flask(__name__)
    @app.route("/")
    def index():
        return "<h1>Bot is running</h1>"
    Thread(target=app.run,args=("0.0.0.0",8080)).start()

filename = 'device_auths.json'
storedlog = []
loadedclients = []
whitelist = []
whitelist_ = []
blacklist = []
blacklist_ = []
otherbotlist = []
client_name = {}
cache_users = {}
blacklist_flag = True
whitelist_flag = True
invitelist_flag = True
otherbotlist_flag = True
discord_flag = True
kill=False
configkeys=["['fortnite']","['fortnite']['email']","['fortnite']['password']","['fortnite']['owner']","['fortnite']['platform']","['fortnite']['cid']","['fortnite']['bid']","['fortnite']['pickaxe_id']","['fortnite']['eid']","['fortnite']['playlist']","['fortnite']['banner']","['fortnite']['banner_color']","['fortnite']['level']","['fortnite']['tier']","['fortnite']['xpboost']","['fortnite']['friendxpboost']","['fortnite']['status']","['fortnite']['privacy']","['fortnite']['whisper']","['fortnite']['partychat']","['fortnite']['disablewhisperperfectly']","['fortnite']['disablepartychatperfectly']","['fortnite']['ignorebot']","['fortnite']['joinmessage']","['fortnite']['randommessage']","['fortnite']['joinmessageenable']","['fortnite']['randommessageenable']","['fortnite']['outfitmimic']","['fortnite']['backpackmimic']","['fortnite']['pickaxemimic']","['fortnite']['emotemimic']","['fortnite']['acceptinvite']","['fortnite']['acceptfriend']","['fortnite']['addfriend']","['fortnite']['invite-ownerdecline']","['fortnite']['inviteinterval']","['fortnite']['interval']","['fortnite']['waitinterval']","['fortnite']['blacklist']","['fortnite']['blacklist-declineinvite']","['fortnite']['blacklist-autoblock']","['fortnite']['blacklist-autokick']","['fortnite']['blacklist-autochatban']","['fortnite']['blacklist-ignorecommand']","['fortnite']['whitelist']","['fortnite']['whitelist-allowinvite']","['fortnite']['whitelist-declineinvite']","['fortnite']['whitelist-ignorelock']","['fortnite']['whitelist-ownercommand']","['fortnite']['invitelist']","['fortnite']['otherbotlist']","['discord']['enabled']","['discord']['token']","['discord']['owner']","['discord']['status']","['discord']['discord']","['discord']['disablediscordperfectly']","['discord']['ignorebot']","['discord']['blacklist']","['discord']['blacklist-ignorecommand']","['discord']['whitelist']","['discord']['whitelist-ignorelock']","['discord']['whitelist-ownercommand']","['lang']","['no-logs']","['ingame-error']","['discord-log']","['hide-email']","['hide-password']","['hide-token']","['hide-webhook']","['webhook']","['caseinsensitive']","['loglevel']","['debug']"]
localizekeys=['bot','lobbybot','credit','library','loglevel','normal','info','debug','debug_is_on','on','off','booting','login','all_login','relogin','owner','party','userid','name_or_id','partyid','content','number','eval','exec','invite_is_decline','restarting','relogining','success','accepted_invite_from','accepted_invite_from2','declined_invite_from','declined_invite_from2','declined_invite_interval','declined_invite_interval2','declined_invite_interval3','declined_invite_owner','declined_invite_owner2','declined_invite_owner3','declined_invite_whitelist','declined_invite_whitelist2','declined_invite_whitelist3','party_member_joined','party_member_left','party_member_request','party_member_kick','party_member_promote','party_member_update','party_member_disconnect','party_member_chatban','party_member_chatban2','party_update','random_message','click_invite','inviteaccept','inviteinterval','invite_from','invite_from2','friend_request_to','friend_request_from','friend_request_decline','friend_accept','friend_add','friend_remove','this_command_owneronly','failed_ownercommand','error_while_declining_partyrequest','error_while_accepting_friendrequest','error_while_declining_friendrequest','error_while_sending_friendrequest','error_while_removing_friendrequest','error_while_removing_friend','error_while_accepting_invite','error_while_declining_invite','error_while_blocking_user','error_while_unblocking_user','error_while_requesting_userinfo','error_while_joining_to_party','error_while_leaving_party','error_while_sending_partyinvite','error_while_changing_asset','error_while_changing_bpinfo','error_while_promoting_party_leader','error_while_kicking_user','error_while_swapping_user','error_while_setting_client','error_already_member_of_party','error_netcl_does_not_match','error_private_party','login_failed','failed_to_load_account','exchange_code_error','api_downing','api_downing2','not_enough_password','owner_notfound','discord_owner_notfound','blacklist_user_notfound','whitelist_user_notfound','discord_blacklist_user_notfound','discord_whitelist_user_notfound','botlist_user_notfound','invitelist_user_notfound','not_friend_with_owner','not_friend_with_inviteuser','not_friend_with_user','nor_pending_with_user','not_party_leader','load_failed_keyerror','load_failed_json','load_failed_notfound','is_missing','too_many_users','too_many_items','user_notfound','user_not_in_party','party_full_or_already_or_offline','party_full_or_already','party_notfound','party_private','not_available','must_be_int','item_notfound','error','add_to_list','already_list','remove_from_list','not_list','enter_to_add_to_list','enter_to_remove_from_list','blacklist','whitelist','discord_blacklist','discord_whitelist','invitelist','botlist','enter_to_get_userinfo','friendcount','pendingcount','outbound','inbound','blockcount','set_to','mimic','outfit','backpack','pet','pickaxe','emote','emoji','toy','command_from','whisper','partychat','discord','disable_perfect','invite','accept','decline','friend_request','join_','message','randommessage','decline_invite_for','enter_to_join_party','party_leave','user_invited','enter_to_invite_user','user_sent','enter_to_send','party_sent','status','banner','bannerid','color','level','bpinfo','tier','xpboost','friendxpboost','privacy','public','friends_allow_friends_of_friends','friends','private_allow_friends_of_friends','private','lastlogin','member_count','enter_to_show_info','itemname','remove_pending','already_friend','enter_to_send_friendrequest','remove_friend','enter_to_remove_friend','enter_to_accept_pending','enter_to_decline_pending','already_block','block_user','enter_to_block_user','not_block','unblock_user','enter_to_unblock_user','optional','reason','chatban_user','already_chatban','enter_to_chatban_user','promote_user','already_party_leader','enter_to_promote_user','kick_user','cant_kick_yourself','readystate','ready','unready','sitout','matchstate','remaining','remaining_must_be_between_0_and_255','swap_user','enter_to_swap_user','lock','stopped','locked','all_end','enter_to_change_asset','setname','no_stylechange','enter_to_set_style','assetpath','set_playlist','please_enter_valid_number']
commandskeys=['ownercommands','true','false','me','prev','eval','exec','restart','relogin','reload','addblacklist','removeblacklist','addwhitelist','removewhitelist','addblacklist_discord','removeblacklist_discord','addwhitelist_discord','removewhitelist_discord','addinvitelist','removeinvitelist','get','friendcount','pendingcount','blockcount','friendlist','pendinglist','blocklist','outfitmimic','backpackmimic','pickaxemimic','emotemimic','whisper','partychat','discord','disablewhisperperfectly','disablepartychatperfectly','disablediscordperfectly','acceptinvite','acceptfriend','joinmessageenable','randommessageenable','wait','join','joinid','leave','invite','inviteall','message','partymessage','status','banner','level','bp','privacy','privacy_public','privacy_friends_allow_friends_of_friends','privacy_friends','privacy_private_allow_friends_of_friends','privacy_private','getuser','getfriend','getpending','getblock','info','info_party','pending','removepending','addfriend','removefriend','acceptpending','declinepending','blockfriend','unblockfriend','chatban','promote','kick','ready','unready','sitout','match','unmatch','swap','outfitlock','backpacklock','pickaxelock','emotelock','stop','alloutfit','allbackpack','allpet','allpickaxe','allemote','allemoji','alltoy','cid','bid','petcarrier','pickaxe_id','eid','emoji_id','toy_id','id','outfit','backpack','pet','pickaxe','emote','emoji','toy','item','set','setvariant','addvariant','setstyle','addstyle','setenlightenment','outfitasset','backpackasset','pickaxeasset','emoteasset']
ignore=['ownercommands','true','false','me', 'privacy_public', 'privacy_friends_allow_friends_of_friends', 'privacy_friends', 'privacy_private_allow_friends_of_friends', 'privacy_private', 'info_party']

def l(key: str, *args: Any, **kwargs: Any) -> Optional[str]:
    text = localize.get(key)
    if text is not None:
        return text.format(*args, **kwargs)
    else:
        return None

def dstore(username: str, content: str) -> None:
    content=str(content)
    if data['hide-email'] is True:
        for email in data['fortnite']['email'].split(','):
            content=content.replace(email,len(email)*"X")
    if data['hide-password'] is True:
        for password in data['fortnite']['password'].split(','):
            content=content.replace(password,len(password)*"X")
    if data['hide-token'] is True:
        for token in data['discord']['token'].split(','):
            content=content.replace(token,len(token)*"X")
    if data['hide-webhook'] is True:
        for webhook in data['webhook'].split(','):
            content=content.replace(webhook,len(webhook)*"X")
    if data['discord-log'] is True:
        if len(storedlog) > 0:
            if list(storedlog[len(storedlog)-1].keys())[0] == username:
                if len(list(storedlog[len(storedlog)-1].values())[0]) + len(content) > 2000:
                    storedlog.append({username: content})
                else:
                    storedlog[len(storedlog)-1][username]+=f'\n{content}'
            else:
                storedlog.append({username: content})
        else:
            storedlog.append({username: content})

def dprint() -> None:
    global kill
    while True:
        if kill is True:
            sys.exit(0)
        if data['discord-log'] is True:
            if len(storedlog) != 0:
                for send in storedlog:
                    try:
                        username=list(send.keys())[0]
                        content=list(send.values())[0]
                        if len(content) > 2000:
                            text=[content[i: i+2000] for i in range(0, len(content), 2000)]
                            for text_ in text:
                                r=requests.post(
                                data['webhook'],
                                json={
                                    'username': username,
                                    'content': text_
                                }
                            )
                        else:
                            r=requests.post(
                                data['webhook'],
                                json={
                                    'username': username,
                                    'content': content
                                }
                            )
                        if data['loglevel'] == 'debug':
                            print(yellow(f'[{r.status_code}] {username}: {content}'))
                        if r.status_code == 204:
                            storedlog.remove(send)
                        if r.status_code == 429:
                            break
                    except TypeError:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore('ボット', f">>> {traceback.format_exc()}")
                        try:
                            storedlog.remove(send)
                        except Exception:
                            pass
                        continue
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore('ボット', f">>> {traceback.format_exc()}")
                        print(yellow(f'{username}: {content} の送信中にエラーが発生しました'))
                        dstore('ボット', f'{username}: {content} の送信中にエラーが発生しました')
                        continue
                time.sleep(5)

def get_device_auth_details() -> None:
    if os.path.isfile(filename):
        with open(filename, 'r') as fp:
            return json.load(fp)
    return {}

def store_device_auth_details(email: str, details: dict) -> None:
    existing = get_device_auth_details()
    existing[email] = details
    with open(filename, 'w') as fp:
        json.dump(existing, fp)

def now_() -> str:
    return datetime.datetime.now().strftime('%H:%M:%S')

def platform_to_str(platform: fortnitepy.Platform) -> Optional[str]:
    if platform is fortnitepy.Platform.WINDOWS:
        return 'Windows'
    elif platform is fortnitepy.Platform.MAC:
        return 'Mac'
    elif platform is fortnitepy.Platform.PLAYSTATION:
        return 'PlayStation'
    elif platform is fortnitepy.Platform.XBOX:
        return 'Xbox'
    elif platform is fortnitepy.Platform.SWITCH:
        return 'Switch'
    elif platform is fortnitepy.Platform.IOS:
        return 'IOS'
    elif platform is fortnitepy.Platform.ANDROID:
        return 'Android'
    else:
        return None

def convert_to_type(text: str) -> Optional[str]:
    if True in [text.lower() in commands[key].split(",") for key in ("cid", "outfit", "alloutfit", "outfitasset")] or text.lower().startswith("cid_"):
        return "outfit"
    elif True in [text.lower() in commands[key].split(",") for key in ("bid", "backpack", "allbackpack", "backpackasset")] or text.lower().startswith("bid_"):
        return "backpack"
    elif True in [text.lower() in commands[key].split(",") for key in ("petcarrier", "pet", "allpet")] or text.lower().startswith("petcarrier_"):
        return "pet"
    elif True in [text.lower() in commands[key].split(",") for key in ("pickaxe_id", "pickaxe", "allpickaxe", "pickaxeasset")] or text.lower().startswith("pickaxe_id"):
        return "pickaxe"
    elif True in [text.lower() in commands[key].split(",") for key in ("eid", "emote", "allemote", "emoteasset")] or text.lower().startswith("eid_"):
        return "emote"
    elif True in [text.lower() in commands[key].split(",") for key in ("emoji_id", "emoji", "allemoji")] or text.lower().startswith("emoji_"):
        return "emoji"
    elif True in [text.lower() in commands[key].split(",") for key in ("toy_id", "toy", "alltoy")] or text.lower().startswith("toy_"):
        return "toy"
    elif True in [text.lower() in commands[key].split(",") for key in ("id", "item")]:
        return "item"

def convert_to_asset(text: str) -> Optional[str]:
    if True in [text.lower() in commands[key].split(",") for key in ("cid", "outfit", "alloutfit", "outfitasset")] or text.lower().startswith("cid_"):
        return "outfit"
    elif True in [text.lower() in commands[key].split(",") for key in ("bid", "backpack", "allbackpack", "backpackasset")] or text.lower().startswith("bid_"):
        return "backpack"
    elif True in [text.lower() in commands[key].split(",") for key in ("petcarrier", "pet", "allpet")] or text.lower().startswith("petcarrier_"):
        return "backpack"
    elif True in [text.lower() in commands[key].split(",") for key in ("pickaxe_id", "pickaxe", "allpickaxe", "pickaxeasset")] or text.lower().startswith("pickaxe_id"):
        return "pickaxe"
    elif True in [text.lower() in commands[key].split(",") for key in ("eid", "emote", "allemote", "emoteasset")] or text.lower().startswith("eid_"):
        return "emote"
    elif True in [text.lower() in commands[key].split(",") for key in ("emoji_id", "emoji", "allemoji")] or text.lower().startswith("emoji_"):
        return "emote"
    elif True in [text.lower() in commands[key].split(",") for key in ("toy_id", "toy", "alltoy")] or text.lower().startswith("toy_"):
        return "emote"

def convert_to_id(text: str) -> Optional[str]:
    if True in [text.lower() in commands[key].split(",") for key in ("cid", "outfit", "alloutfit", "outfitasset")] or text.lower().startswith("cid_"):
        return "cid"
    elif True in [text.lower() in commands[key].split(",") for key in ("bid", "backpack", "allbackpack", "backpackasset")] or text.lower().startswith("bid_"):
        return "bid"
    elif True in [text.lower() in commands[key].split(",") for key in ("petcarrier", "pet", "allpet")] or text.lower().startswith("petcarrier_"):
        return "petcarrier"
    elif True in [text.lower() in commands[key].split(",") for key in ("pickaxe_id", "pickaxe", "allpickaxe", "pickaxeasset")] or text.lower().startswith("pickaxe_id"):
        return "pickaxe_id"
    elif True in [text.lower() in commands[key].split(",") for key in ("eid", "emote", "allemote", "emoteasset")] or text.lower().startswith("eid_"):
        return "eid"
    elif True in [text.lower() in commands[key].split(",") for key in ("emoji_id", "emoji", "allemoji")] or text.lower().startswith("emoji_"):
        return "emoji_id"
    elif True in [text.lower() in commands[key].split(",") for key in ("toy_id", "toy", "alltoy")] or text.lower().startswith("toy_"):
        return "toy_id"
    elif True in [text.lower() in commands[key].split(",") for key in ("id", "item")]:
        return "id"

def convert_variant(type_: str, variants: dict) -> List[dict]:
    result = []
    for variant in variants:
        for option in variant['options']:
            result.append({"name": option['name'], 'variants': [{'item': type_, 'channel': variant['channel'], 'variant': option['tag']}]})
    return result

def inviteaccept(client: fortnitepy.Client) -> None:
    if data['no-logs'] is False:
        print(f'[{now_()}] [{client.user.display_name}] {l("inviteaccept")}')
    dstore(client.user.display_name, f'{l("inviteaccept")}')
    client.acceptinvite=True

def inviteinterval(client: fortnitepy.Client) -> None:
    if data['no-logs'] is False:
        print(f'[{now_()}] [{client.user.display_name}] {l("inviteinterval")}')
    dstore(client.user.display_name, f'{l("inviteinterval")}')
    client.acceptinvite_interval=True

def reload_configs(client: fortnitepy.Client) -> bool:
    global data
    global commands
    try:
        try:
            with open('config.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.decoder.JSONDecodeError:
            with open('config.json', 'r', encoding='utf-8-sig') as f:
                data = json.load(f)
        if data['loglevel'] == 'debug':
            print(yellow(f'\n{data}\n'))
            dstore(l("bot"),f'\n```\n{data}\n```\n')
        for key in configkeys:
            exec(f"errorcheck=data{key}")
        flag = False
        try:
            errorcheck=requests.get('https://fortnite-api.com/cosmetics/br/search?name=API-KEY-CHECK',headers={'x-api-key': data['api-key']}).json()
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(l("bot"),f'>>> {traceback.format_exc()}')
            flag = True
        else:
            if errorcheck['status'] == 503:
                flag = True
        if flag is True:
            if os.path.isfile('allen.json') is False or os.path.isfile('allja.json') is False:
                print(red(l("api_downing")))
                dstore(l("bot"),f'>>> {l("api_downing")}')
                return False
            else:
                print(red(l("api_downing2")))
                dstore(l("bot"),f'>>> {l("api_downing2")}')
                return False
        credentials={}
        try:
            for count,mail in enumerate(data['fortnite']['email'].split(',')):
                credentials[mail]=data['fortnite']['password'].split(',')[count]
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
            print(red(l("not_enough_password")))
            dstore(l("bot"),f'>>> {l("not_enough_password")}')
    except KeyError as e:
        print(red(traceback.format_exc()))
        print(red(l("load_failed_keyerror", "config.json")))
        print(red(l("is_missing", str(e))))
        dstore(l("bot"),f'>>> {traceback.format_exc()}')
        dstore(l("bot"),f'>>> {l("load_failed_keyerror", "config.json")}')
        dstore(l("bot"),f'>>> {l("is_missing", str(e))}')
        return False
    except json.decoder.JSONDecodeError as e:
        print(red(traceback.format_exc()))
        print(red(str(e)))
        print(red(l("load_failed_json", "config.json")))
        dstore(l("bot"),f'>>> {traceback.format_exc()}')
        dstore(l("bot"),f'>>> {str(e)}')
        dstore(l("bot"),f'>>> {l("load_failed_json", "config.json")}')
        return False
    except FileNotFoundError:
        print(red(traceback.format_exc()))
        print(red(l("load_failed_notfound", "config.json")))
        dstore(l("bot"),f'>>> {traceback.format_exc()}')
        dstore(l("bot"),f'>>> {l("load_failed_notfound", "config.json")}')
        return False

    if os.path.isfile(f"lang/{data['lang']}.json"):
        try:
            try:
                with open(f'lang/{data["lang"]}.json', 'r', encoding='utf-8') as f:
                    localize = json.load(f)
            except json.decoder.JSONDecodeError:
                with open(f'lang/{data["lang"]}.json', 'r', encoding='utf-8-sig') as f:
                    localize = json.load(f)
            if data['loglevel'] == 'debug':
                print(yellow(f'\n{localize}\n'))
                dstore(l("bot"),f'\n```\n{localize}\n```\n')
            for key in localizekeys:
                exec(f"errorcheck=localize['{key}']")
        except KeyError as e:
            print(red(traceback.format_exc()))
            print(red(l("load_failed_keyerror", f"{data['lang']}.json")))
            print(red(l("is_missing", str(e))))
            dstore(l("bot"),f'>>> {traceback.format_exc()}')
            dstore(l("bot"),f'>>> {l("load_failed_keyerror", f"""{data["lang"]}.json""")}')
            dstore(l("bot"),f'>>> {l("is_missing", str(e))}')
            return False
        except json.decoder.JSONDecodeError as e:
            print(red(traceback.format_exc()))
            print(red(str(e)))
            print(red(l("load_failed_json", f"{data['lang']}.json")))
            dstore(l("bot"),f'>>> {traceback.format_exc()}')
            dstore(l("bot"),f'>>> {str(e)}')
            dstore(l("bot"),f'>>> {l("load_failed_json", f"""{data["lang"]}.json""")}')
            return False
        except FileNotFoundError:
            print(red(traceback.format_exc()))
            print(red(l("load_failed_notfound", f"{data['lang']}.json")))
            dstore(l("bot"),f'>>> {traceback.format_exc()}')
            dstore(l("bot"),f'>>> {l("load_failed_notfound", f"""{data["lang"]}.json""")}')
            return False
    else:
        try:
            try:
                with open('lang/en.json', 'r', encoding='utf-8') as f:
                    localize = json.load(f)
            except json.decoder.JSONDecodeError:
                with open('lang/en.json', 'r', encoding='utf-8-sig') as f:
                    localize = json.load(f)
            if data['loglevel'] == 'debug':
                print(yellow(f'\n{localize}\n'))
                dstore(l("bot"),f'\n```\n{localize}\n```\n')
            for key in localizekeys:
                exec(f"errorcheck=localize['{key}']")
        except KeyError as e:
            print(red(traceback.format_exc()))
            print(red(l("load_failed_keyerror", f"en.json")))
            print(red(l("is_missing", str(e))))
            dstore(l("bot"),f'>>> {traceback.format_exc()}')
            dstore(l("bot"),f'>>> {l("load_failed_keyerror", f"""en.json""")}')
            dstore(l("bot"),f'>>> {l("is_missing", str(e))}')
            return False
        except json.decoder.JSONDecodeError as e:
            print(red(traceback.format_exc()))
            print(red(str(e)))
            print(red(l("load_failed_json", f"en.json")))
            dstore(l("bot"),f'>>> {traceback.format_exc()}')
            dstore(l("bot"),f'>>> {str(e)}')
            dstore(l("bot"),f'>>> {l("load_failed_json", f"""en.json""")}')
            return False
        except FileNotFoundError:
            print(red(traceback.format_exc()))
            print(red(l("load_failed_notfound", f"en.json")))
            dstore(l("bot"),f'>>> {traceback.format_exc()}')
            dstore(l("bot"),f'>>> {l("load_failed_notfound", f"""en.json""")}')
            return False

    threading.Thread(target=get_item_info,args=()).start()
    if True:
        if data['fortnite']['whisper'] not in (True, False):
            data['fortnite']['whisper'] = True
        if data['fortnite']['partychat'] not in (True, False):
            data['fortnite']['partychat'] = True
        if data['fortnite']['disablewhisperperfectly'] not in (True, False):
            data['fortnite']['disablewhisperperfectly'] = False
        if data['fortnite']['disablepartychatperfectly'] not in (True, False):
            data['fortnite']['disablepartychatperfectly'] = False
        if data['fortnite']['joinmessageenable'] not in (True, False):
            data['fortnite']['joinmessageenable'] = False
        if data['fortnite']['randommessageenable'] not in (True, False):
            data['fortnite']['randommessageenable'] = False
        if data['fortnite']['outfitmimic'] not in (True, False):
            data['fortnite']['outfitmimic'] = False
        if data['fortnite']['backpackmimic'] not in (True, False):
            data['fortnite']['backpackmimic'] = False
        if data['fortnite']['pickaxemimic'] not in (True, False):
            data['fortnite']['pickaxemimic'] = False
        if data['fortnite']['emotemimic'] not in (True, False):
            data['fortnite']['emotemimic'] = False
        if data['fortnite']['acceptinvite'] not in (True, False):
            data['fortnite']['acceptinvite'] = True
        if data['fortnite']['acceptfriend'] not in (True, False, None):
            data['fortnite']['acceptfriend'] = True
        if data['fortnite']['addfriend'] not in (True, False):
            data['fortnite']['addfriend'] = False
        if data['fortnite']['invite-ownerdecline'] not in (True, False):
            data['fortnite']['invite-ownerdecline'] = False
        if data['fortnite']['inviteinterval'] not in (True, False):
            data['fortnite']['inviteinterval'] = False
        if data['fortnite']['blacklist-declineinvite'] not in (True, False):
            data['fortnite']['blacklist-declineinvite'] = False
        if data['fortnite']['blacklist-autoblock'] not in (True, False):
            data['fortnite']['blacklist-autoblock'] = False
        if data['fortnite']['blacklist-autokick'] not in (True, False):
            data['fortnite']['blacklist-autokick'] = False
        if data['fortnite']['blacklist-autochatban'] not in (True, False):
            data['fortnite']['blacklist-autochatban'] = False
        if data['fortnite']['blacklist-ignorecommand'] not in (True, False):
            data['fortnite']['blacklist-ignorecommand'] = False
        if data['fortnite']['whitelist-allowinvite'] not in (True, False):
            data['fortnite']['whitelist-allowinvite'] = False
        if data['fortnite']['whitelist-declineinvite'] not in (True, False):
            data['fortnite']['whitelist-declineinvite'] = False
        if data['fortnite']['whitelist-ignorelock'] not in (True, False):
            data['fortnite']['whitelist-ignorelock'] = False
        if data['fortnite']['whitelist-ownercommand'] not in (True, False):
            data['fortnite']['whitelist-ownercommand'] = False

    if True:
        if data['discord']['enabled'] not in (True, False):
            data['discord']['enabled'] = False
        if data['discord']['discord'] not in (True, False):
            data['discord']['discord'] = True
        if data['discord']['disablediscordperfectly'] not in (True, False):
            data['discord']['disablediscordperfectly'] = True
        if data['discord']['blacklist-ignorecommand'] not in (True, False):
            data['discord']['blacklist-ignorecommand'] = False
        if data['discord']['whitelist-ignorelock'] not in (True, False):
            data['discord']['whitelist-ignorelock'] = False
        if data['discord']['whitelist-ownercommand'] not in (True, False):
            data['discord']['whitelist-ownercommand'] = False

    if True:
        if data['no-logs'] not in (True, False):
            data['no-logs'] = False
        if data['ingame-error'] not in (True, False):
            data['ingame-error'] = True
        if data['discord-log'] not in (True, False):
            data['discord-log'] = False
        if data['hide-email'] not in (True, False):
            data['hide-email'] = True
        if data['hide-password'] not in (True, False):
            data['hide-password'] = True
        if data['hide-webhook'] not in (True, False):
            data['hide-webhook'] = True
        if data['hide-api-key'] not in (True, False):
            data['hide-api-key'] = True
        if data['caseinsensitive'] not in (True, False):
            data['caseinsensitive'] = True
        if data['loglevel'] not in ('normal', 'info', 'debug'):
            data['loglevel'] = 'normal'
        if data['fortnite']['privacy'] not in ('public', 'friends_allow_friends_of_friends', 'friends', 'private_allow_friends_of_friends', 'private'):
            data['fortnite']['privacy'] = 'public'

    data['fortnite']['privacy']=eval(f"fortnitepy.PartyPrivacy.{data['fortnite']['privacy'].upper()}")
    client.whisper=data['fortnite']['whisper']
    client.partychat=data['fortnite']['partychat']
    client.discord=data['discord']['discord']
    client.whisperperfect=data['fortnite']['disablewhisperperfectly']
    client.partychatperfect=data['fortnite']['disablepartychatperfectly']
    client.discordperfect=data['discord']['disablediscordperfectly']
    client.joinmessageenable=data['fortnite']['joinmessageenable']
    client.randommessageenable=data['fortnite']['randommessageenable']
    client.outfitmimic=data['fortnite']['outfitmimic']
    client.backpackmimic=data['fortnite']['backpackmimic']
    client.pickaxemimic=data['fortnite']['pickaxemimic']
    client.emotemimic=data['fortnite']['emotemimic']
    client.acceptinvite=data['fortnite']['acceptinvite']
    client.acceptfriend=data['fortnite']['acceptfriend']

    try:
        try:
            with open('commands.json', 'r', encoding='utf-8') as f:
                commands=json.load(f)
        except json.decoder.JSONDecodeError:
            with open('commands.json', 'r', encoding='utf-8-sig') as f:
                commands=json.load(f)
        if data['loglevel'] == 'debug':
            print(yellow(f'\n{commands}\n'))
            dstore(l("bot"),f'\n```\n{commands}\n```\n')
        for key in commandskeys:
            exec(f"errorcheck=commands['{key}']")
        if data['caseinsensitive'] is True:
            commands=dict((k.lower(), jaconv.kata2hira(v.lower())) for k,v in commands.items())
        for checks in commands.items():
            if checks[0] in ignore:
                continue
            if commands['ownercommands'] == '':
                break
            for command in commands['ownercommands'].split(','):
                try:
                    errorcheck=commands[command.lower()]
                except KeyError as e:
                    print(red(traceback.format_exc()))
                    print(red(l("failed_ownercommand")))
                    print(red(l("is_missing", str(e))))
                    dstore(l("bot"),f'>>> {traceback.format_exc()}')
                    dstore(l("bot"),f'>>> {l("failed_ownercommand")}')
                    dstore(l("bot"),f'>>> {l("is_missing", str(e))}')
                    return False
    except KeyError as e:
        print(red(traceback.format_exc()))
        print(red(l("load_failed_keyerror", "commands.json")))
        print(red(l("is_missing", str(e))))
        dstore(l("bot"),f'>>> {traceback.format_exc()}')
        dstore(l("bot"),f'>>> {l("load_failed_keyerror", "commands.json")}')
        dstore(l("bot"),f'>>> {l("is_missing", str(e))}')
        return False
    except json.decoder.JSONDecodeError as e:
        print(red(traceback.format_exc()))
        print(red(str(e)))
        print(red(l("load_failed_json", "commands.json")))
        dstore(l("bot"),f'>>> {traceback.format_exc()}')
        dstore(l("bot"),f'>>> {str(e)}')
        dstore(l("bot"),f'>>> {l("load_failed_json", "commands.json")}')
        return False
    except FileNotFoundError:
        print(red(traceback.format_exc()))
        print(red(l("load_failed_notfound", "commands.json")))
        dstore(l("bot"),f'>>> {traceback.format_exc()}')
        dstore(l("bot"),f'>>> {l("load_failed_notfound", "commands.json")}')
        return False

    try:
        try:
            with open('replies.json', 'r', encoding='utf-8') as f:
                replies=json.load(f)
        except json.decoder.JSONDecodeError:
            with open('replies.json', 'r', encoding='utf-8-sig') as f:
                replies=json.load(f)
        if data['loglevel'] == 'debug':
            print(yellow(f'\n{replies}\n'))
            dstore(l("bot"),f'\n```\n{replies}\n```\n')
        if data['caseinsensitive'] is True:
            replies=dict((jaconv.kata2hira(k.lower()), v) for k,v in replies.items())
    except json.decoder.JSONDecodeError as e:
        print(red(traceback.format_exc()))
        print(red(str(e)))
        print(red(l("load_failed_json", "replies.json")))
        dstore(l("bot"),f'>>> {traceback.format_exc()}')
        dstore(l("bot"),f'>>> {str(e)}')
        dstore(l("bot"),f'>>> {l("load_failed_json", "replies.json")}')
        return False
    except FileNotFoundError:
        print(red(traceback.format_exc()))
        print(red(l("load_failed_notfound", "replies.json")))
        dstore(l("bot"),f'>>> {traceback.format_exc()}')
        dstore(l("bot"),f'>>> {l("load_failed_notfound", "replies.json")}')
        return False

    return True

def get_item_info() -> None:
    try:
        req=requests.get('https://fortnite-api.com/v2/cosmetics/br?language=en')
        if data['loglevel'] == 'debug':
            print(yellow(f'\n[{req.status_code}] {req.url}\n{req.text[:100]}'))
            dstore(l("bot"),f'```\n[{req.status_code}] {req.url}\n{req.text[:100]}\n```')
        allcosmen=req.json()
        if req.status_code == 200:
            with open('allen.json', 'w') as f:
                json.dump(allcosmen, f)
        req=requests.get(f'https://fortnite-api.com/v2/cosmetics/br?language={data["lang"]}')
        if data['loglevel'] == 'debug':
            print(yellow(f'[{req.status_code}] {req.url}\n{req.text[:100]}'))
            dstore(l("bot"),f'```\n[{req.status_code}] {req.url}\n{req.text[:100]}\n```')
        allcosm=req.json()
        if req.status_code == 200:
            with open(f'all{data["lang"]}.json', 'w') as f:
                json.dump(allcosm, f)
    except UnicodeEncodeError:
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(l("bot"),f'>>> {traceback.format_exc()}')
    except Exception:
        print(red(traceback.format_exc()))
        dstore(l("bot"),f'>>> {traceback.format_exc()}')

def add_cache(client: fortnitepy.Client, user: Type[fortnitepy.user.UserBase]) -> None:
    try:
        if isinstance(user, fortnitepy.user.UserBase) and user.id is not None:
            if isinstance(user, fortnitepy.User):
                if user.display_name is not None:
                    cache_users[user.display_name] = user
            else:
                user = client.get_user(user.id)
                if user is not None:
                    if user.display_name is not None:
                        cache_users[user.display_name] = user
    except Exception:
        print(red(traceback.format_exc()))
        dstore(l("bot"),f'>>> {traceback.format_exc()}')

def partymember_backpack(member: Type[fortnitepy.party.PartyMemberBase]) -> str:
    asset = member.meta.get_prop("AthenaCosmeticLoadout_j")["AthenaCosmeticLoadout"]["backpackDef"]
    result = re.search(r".*\.([^\'\"]*)", asset.strip("'"))
    if result is not None and result.group(1) != 'None':
        return result.group(1)

def partymember_emote(member: Type[fortnitepy.party.PartyMemberBase]) -> str:
    asset = member.meta.get_prop("FrontendEmote_j")["FrontendEmote"]["emoteItemDef"]
    result = re.search(r".*\.([^\'\"]*)", asset.strip("'"))
    if result is not None and result.group(1) != 'None':
        return result.group(1)

def member_asset(member: Type[fortnitepy.party.PartyMemberBase], asset: str) -> str:
    if asset in ("backpack", "pet"):
        return partymember_backpack(member)
    elif asset in ("emote", "emoji", "toy"):
        return partymember_emote(member)
    else:
        return eval(f"member.{asset}")

def lock_check(client: fortnitepy.Client, author_id: str) -> bool:
    if client.owner is not None:
        if data['fortnite']['whitelist-ignorelock']:
            if client.owner.id != author_id and author_id not in whitelist:
                return True
        else:
            if client.owner.id != author_id:
                return True
    else:
        if data['fortnite']['whitelist-ignorelock']:
            if author_id not in whitelist:
                return True
        else:
            return True
    return False

def search_item(lang: str, mode: str, text: str, type_: str = None) -> List[dict]:
    ignoretype = [
        "banner",
        "contrail",
        "glider",
        "wrap",
        "loadingscreen",
        "music",
        "spray"
    ]
    itemlist = []
    with open(f'all{lang}.json', 'r', encoding='utf-8') as f:
        data_ = json.load(f)
    for item in data_['data']:
        if item['type']['value'] in ignoretype:
            continue
        if mode == "name":
            if data['caseinsensitive'] is True:
                text=jaconv.hira2kata(text.lower())
                name=jaconv.hira2kata(item['name'].lower())
            else:
                name=item['name']
            if text in name:
                if type_ in (None, "item"):
                    itemlist.append(item)
                else:
                    if item['type']['value'] in type_.split(','):
                        itemlist.append(item)
        elif mode == "id":
            if text.lower() in item['id'].lower():
                if type_ in (None, "item"):
                    itemlist.append(item)
                else:
                    if item['type']['value'] in type_.split(','):
                        itemlist.append(item)
        elif mode == "set":
            if item.get('set') is None:
                continue
            if data['caseinsensitive'] is True:
                text=jaconv.hira2kata(text.lower())
                name=jaconv.hira2kata(item['set']['value'].lower())
            else:
                name=item['set']['value']
            if text in name:
                if type_ in (None, "item"):
                    itemlist.append(item)
                else:
                    if item['type']['value'] in type_.split(','):
                        itemlist.append(item)
    if data['loglevel'] == 'debug':
        print(yellow(f'{lang} {type_}: {text}\n{itemlist}'))
        dstore(l("bot"),f'```\n{lang} {type_}: {text}\n{itemlist}\n```')
    if len(itemlist) == 0:
        return None
    else:
        return itemlist

def search_style(lang: str, id_: str) -> Optional[List[dict]]:
    with open(f'all{lang}.json', 'r', encoding='utf-8') as f:
        data_ = json.load(f)
    for item in data_['data']:
        if item['id'].lower() == id_.lower():
            if item['variants'] is not None:
                variants = convert_variant(item['backendType'], item['variants'])
    print(yellow(f'{id_}: {variants}'))
    if len(variants) == 0:
        return None
    else:
        return variants

async def reply(message: Union[Type[fortnitepy.message.MessageBase], Type[discord.Message]], content: str) -> None:
    if isinstance(message, fortnitepy.message.MessageBase) is True:
        await message.reply(content)
    elif isinstance(message, discord.Message) is True:
        await message.channel.send(content)

async def change_asset(client: fortnitepy.Client, author_id: str, type_: str, id_: str, variants_: dict = {}, enlightenment: Union[tuple, list] = []) -> None:
    global blacklist
    global blacklist_
    global whitelist
    global whitelist_
    if not enlightenment:
        enlightenment = None
    if type_ == "outfit":
        flag = False
        if client.outfitlock is True:
            flag = lock_check(client, author_id)
        if flag is True:
            return False
        else:
            if 'banner' in id_:
                variants = client.party.me.create_variants(item="AthenaCharacter", profile_banner='ProfileBanner')
                variants += variants_ 
            else:
                variants = variants_
            await client.party.me.edit_and_keep(partial(client.party.me.set_outfit, asset=id_, variants=variants, enlightenment=enlightenment))
    elif type_ == "backpack":
        flag = False
        if client.backpacklock is True:
            flag = lock_check(client, author_id)
        if flag is True:
            return False
        else:
            if 'banner' in id_:
                variants = client.party.me.create_variants(item="AthenaBackpack", profile_banner='ProfileBanner')
                variants += variants_ 
            else:
                variants = variants_
            await client.party.me.edit_and_keep(partial(client.party.me.set_backpack, asset=id_, variants=variants, enlightenment=enlightenment))
    elif type_ == "pet":
        flag = False
        if client.backpacklock is True:
            flag = lock_check(client, author_id)
        if flag is True:
            return False
        else:
            if 'banner' in id_:
                variants = client.party.me.create_variants(item="AthenaBackpack", profile_banner='ProfileBanner')
                variants += variants_ 
            else:
                variants = variants_
            await client.party.me.edit_and_keep(partial(client.party.me.set_pet, asset=id_, variants=variants))
    elif type_ == "pickaxe":
        flag = False
        if client.pickaxelock is True:
            flag = lock_check(client, author_id)
        if flag is True:
            return False
        else:
            if 'banner' in id_:
                variants = client.party.me.create_variants(item="AthenaPickaxe", profile_banner='ProfileBanner')
                variants += variants_ 
            else:
                variants = variants_
            await client.party.me.edit_and_keep(partial(client.party.me.set_pickaxe, asset=id_, variants=variants))
    elif type_ == "emote":
        flag = False
        if client.emotelock is True:
            flag = lock_check(client, author_id)
        if flag is True:
            return False
        else:
            if client.party.me.emote is not None:
                if client.party.me.emote.lower() == id_.lower():
                    await client.party.me.clear_emote()
            await client.party.me.set_emote(asset=id_)
            client.eid=id_
    elif type_ == "emoji":
        flag = False
        if client.emotelock is True:
            flag = lock_check(client, author_id)
        if flag is True:
            return False
        else:
            if client.party.me.emote is not None:
                if client.party.me.emote.lower() == id_.lower():
                    await client.party.me.clear_emote()
            id_ = f"/Game/Athena/Items/Cosmetics/Dances/Emoji/{id_}.{id_}"
            await client.party.me.set_emote(asset=id_)
            client.eid=id_
    elif type_ == "toy":
        flag = False
        if client.emotelock is True:
            flag = lock_check(client, author_id)
        if flag is True:
            return False
        else:
            if client.party.me.emote is not None:
                if client.party.me.emote.lower() == id_.lower():
                    await client.party.me.clear_emote()
            id_ = f"/Game/Athena/Items/Cosmetics/Toys/{id_}.{id_}"
            await client.party.me.set_emote(asset=id_)
            client.eid=id_
    return True

async def invitation_accept(invitation: fortnitepy.ReceivedPartyInvitation) -> None:
    client=invitation.client
    try:
        await invitation.accept()
        client.acceptinvite_interval=False
        try:
            client.timer.cancel()
        except Exception:
            pass
        client.timer=Timer(data['fortnite']['interval'], inviteinterval, [client])
        client.timer.start()
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(f'[{now_()}] [{client.user.display_name}] {l("accepted_invite_from", str(invitation.sender.display_name))}')
            dstore(client.user.display_name,l("accepted_invite_from", str(invitation.sender.display_name)))
        else:
            if data['no-logs'] is False:
                print(f'[{now_()}] [{client.user.display_name}] {l("accepted_invite_from2", f"{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}]", invitation.party.id)}')
            dstore(client.user.display_name,l("accepted_invite_from2", f"{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}]", invitation.party.id))
    except KeyError:
        if data['ingame-error'] is True:
            await invitation.sender.send(l("error"))
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    except fortnitepy.PartyError:
        if data['ingame-error'] is True:
            await invitation.sender.send(l("error_already_member_of_party"))
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] {l("already_member_of_party")}'))
        dstore(client.user.display_name,f'>>> {l("already_member_of_party")}')
    except fortnitepy.HTTPException:
        if data['ingame-error'] is True:
            await invitation.sender.send(l("user_notfound"))
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] {l("user_notfound")}'))
        dstore(client.user.display_name,f'>>> {l("user_notfound")}')
    except fortnitepy.Forbidden:
        if data['ingame-error'] is True:
            await invitation.sender.send(l("error_private_party"))
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] {l("error_private_party")}'))
        dstore(client.user.display_name,f'>>> {l("error_private_party")}')
    except fortnitepy.HTTPException:
        if data['ingame-error'] is True:
            await invitation.sender.send(l("error_while_accepting_partyinvite"))
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_accepting_partyinvite")}'))
        dstore(client.user.display_name,f'>>> {l("error_while_accepting_partyinvite")}')
    except Exception:
        if data['ingame-error'] is True:
            await invitation.sender.send(l("error"))
        print(red(traceback.format_exc()))
        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

async def invitation_decline(invitation: fortnitepy.ReceivedPartyInvitation) -> None:
    client=invitation.client
    try:
        await invitation.decline()
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(f'[{now_()}] [{client.user.display_name}] {l("declined_invite_from", str(invitation.sender.display_name))}')
            dstore(client.user.display_name,l("declined_invite_from", str(invitation.sender.display_name)))
        else:
            if data['no-logs'] is False:
                print(f'[{now_()}] [{client.user.display_name}] {l("declined_invite_from2", f"{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}]", invitation.party.id)}')
            dstore(client.user.display_name,l("declined_invite_from2", f"{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}]", invitation.party.id))
    except fortnitepy.PartyError:
        if data['ingame-error'] is True:
            await invitation.sender.send(l("error_netcl_does_not_match"))
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] {l("error_netcl_does_not_match")}'))
        dstore(client.user.display_name,f'>>> {l("error_netcl_does_not_match")}')
    except fortnitepy.HTTPException:
        if data['ingame-error'] is True:
            await invitation.sender.send(l("error_while_declining_invite"))
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_declining_invite")}'))
        dstore(client.user.display_name,f'>>> {l("error_while_declining_invite")}')
    except Exception:
        if data['ingame-error'] is True:
            await invitation.sender.send(l("error"))
        print(red(traceback.format_exc()))
        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

async def invitation_decline_interval(invitation: fortnitepy.ReceivedPartyInvitation) -> None:
    client=invitation.client
    try:
        await invitation.decline()
        await invitation.sender.send(l("declined_invite_interval3"))
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(f'[{now_()}] [{client.user.display_name}] {l("declined_invite_interval", str(invitation.sender.display_name), str(data["fortnite"]["interval"]))}')
            dstore(client.user.display_name,l("declined_invite_interval", str(invitation.sender.display_name), str(data["fortnite"]["interval"])))
        else:
            if data['no-logs'] is False:
                print(f'[{now_()}] [{client.user.display_name}] {l("declined_invite_interval2", f"{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}]", invitation.party.id, str(data["fortnite"]["interval"]))}')
            dstore(client.user.display_name,l("declined_invite_interval2", f"{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}]", invitation.party.id, str(data['fortnite']['interval'])))
    except fortnitepy.PartyError:
        if data['ingame-error'] is True:
            await invitation.sender.send(l("error_netcl_does_not_match"))
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] {l("error_netcl_does_not_match")}'))
        dstore(client.user.display_name,f'>>> {l("error_netcl_does_not_match")}')
    except fortnitepy.HTTPException:
        if data['ingame-error'] is True:
            await invitation.sender.send(l("error_while_declining_invite"))
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_declining_invite")}'))
        dstore(client.user.display_name,f'>>> {l("error_while_declining_invite")}')
    except Exception:
        if data['ingame-error'] is True:
            await invitation.sender.send(l("error"))
        print(red(traceback.format_exc()))
        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

async def invitation_decline_owner(invitation: fortnitepy.ReceivedPartyInvitation) -> None:
    try:
        await invitation.decline()
        await invitation.sender.send(l("declined_invite_owner3"))
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(f'[{now_()}] [{client.user.display_name}] {l("declined_invite_owner", str(invitation.sender.display_name))}')
            dstore(client.user.display_name,l("declined_invite_owner", str(invitation.sender.display_name)))
        else:
            if data['no-logs'] is False:
                print(f'[{now_()}] [{client.user.display_name}] {l("declined_invite_owner2", f"{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}]", invitation.party.id)}')
            dstore(client.user.display_name,l("declined_invite_owner2", f"{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}]", invitation.party.id))
    except fortnitepy.PartyError:
        if data['ingame-error'] is True:
            await invitation.sender.send(l("error_netch_does_not_match"))
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] {l("error_netch_does_not_match")}'))
        dstore(client.user.display_name,f'>>> {l("error_netch_does_not_match")}')
    except fortnitepy.HTTPException:
        if data['ingame-error'] is True:
            await invitation.sender.send(l("error_while_declining_invite"))
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_declining_invite")}'))
        dstore(client.user.display_name,f'>>> {l("error_while_declining_invite")}')
    except Exception:
        if data['ingame-error'] is True:
            await invitation.sender.send(l("error"))
        print(red(traceback.format_exc()))
        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

async def invitation_decline_whitelist(invitation: fortnitepy.ReceivedPartyInvitation) -> None:
    try:
        await invitation.decline()
        await invitation.sender.send(l("declined_invite_whitelist3"))
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(f'[{now_()}] [{client.user.display_name}] {l("declined_invite_whitelist", str(invitation.sender.display_name))}')
            dstore(client.user.display_name,l("declined_invite_whitelist", str(invitation.sender.display_name)))
        else:
            if data['no-logs'] is False:
                print(f'[{now_()}] [{client.user.display_name}] {l("declined_invite_whitelist2", f"{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}]", invitation.party.id)}')
            dstore(client.user.display_name,l("declined_invite_whitelist2", f"{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}]", invitation.party.id))
    except fortnitepy.PartyError:
        if data['ingame-error'] is True:
            await invitation.sender.send(l("error_netcl_does_not_match"))
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] {l("error_netcl_does_not_match")}'))
        dstore(client.user.display_name,f'>>> {l("error_netcl_does_not_match")}')
    except fortnitepy.HTTPException:
        if data['ingame-error'] is True:
            await invitation.sender.send(l("error_while_declining_invite"))
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_declining_invite")}'))
        dstore(client.user.display_name,f'>>> {l("error_while_declining_invite")}')
    except Exception:
        if data['ingame-error'] is True:
            await invitation.sender.send(l("error"))
        print(red(traceback.format_exc()))
        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

async def aexec(code: str, variable: dict) -> Any:
    _ = lambda l: re.match(r"(\u0020|\u3000)*", l).end() * u"\u0020"
    scode = code.split('\n')
    delete = len(_(scode[0]))
    lines = [i.replace(u"\u0020", "", delete) for i in scode]
    exc = (
        f'async def __ex(var):'
        + '\n for v in var:'
        + '\n     v = var[v]'
        + ''.join(f'\n {l}' for l in lines)
        + '\n for v in locals():'
        + '\n     var[v] = locals()[v]'
    )
    if data['loglevel'] == 'debug':
        print(exc)
    exec(exc)
    variable_before = variable.copy()
    result = await locals()['__ex'](variable)
    variable_after = variable.copy()
    newvar = {k: v for k,v in variable_after.items() if (k not in variable_before.keys() or v != variable_before.get(k)) and "_" not in k and k not in ("k", "v") and isinstance(k, str) is True}
    for k in newvar:
        exc = (
            f"global {k}"
            + f"\n{k} = newvar['{k}']"
        )
        exec(exc)
    return result


try:
    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.decoder.JSONDecodeError:
        with open('config.json', 'r', encoding='utf-8-sig') as f:
            data = json.load(f)
    if data['loglevel'] == 'debug':
        print(yellow(f'\n{data}\n'))
        dstore('ボット',f'\n```\n{data}\n```\n')
    for key in configkeys:
        exec(f"errorcheck=data{key}")
    flag = False
    try:
        errorcheck=requests.get('https://fortnite-api.com/v2/cosmetics/br/DOWN_CHECK').json()
    except Exception:
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore("Bot",f'>>> {traceback.format_exc()}')
        flag = True
    else:
        if errorcheck['status'] == 503:
            flag = True
    if flag is True:
        if os.path.isfile('allen.json') is False or os.path.isfile('allja.json') is False:
            print(red('APIがダウンしています。しばらく待ってからもう一度起動してみてください。'))
            print(red('API is dawning. Please try again later.'))
            dstore('ボット',f'>>> APIがダウンしています。しばらく待ってからもう一度起動してみてください。')
            dstore('Bot',f'>>> API is dawning. Please try again later.')
            sys.exit(1)
        else:
            print(red('APIがダウンしているため、最新のアイテムデータをダウンロードできませんでした。しばらく待ってからもう一度起動してみてください。'))
            print(red('Failed to download latest item data because API is dawning. Please try again later.'))
            dstore('ボット',f'>>> APIがダウンしているため、最新のアイテムデータをダウンロードできませんでした。しばらく待ってからもう一度起動してみてください。')
            dstore('Bot',f'>>> Failed to download latest item data because API is dawning. Please try again later.')
                
    credentials={}
    try:
        for count,mail in enumerate(data['fortnite']['email'].split(',')):
            credentials[mail]=data['fortnite']['password'].split(',')[count]
    except IndexError:
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
        print(red('メールアドレスの数に対しパスワードの数が足りません。読み込めたアカウントのみ起動されます。'))
        print(red('There are not enough passwords for the number of email addresses. Boot only loaded accounts.'))
        dstore('ボット',f'>>> メールアドレスの数に対しパスワードの数が足りません。読み込めたアカウントのみ起動されます。')
        dstore('Bot',f'>>> There are not enough passwords for the number of email addresses. Boot only loaded accounts.')
except KeyError as e:
    print(red(traceback.format_exc()))
    print(red('config.json ファイルの読み込みに失敗しました。キーの名前が間違っていないか確認してください。アップデート後の場合は、最新のconfig.jsonファイルを確認してください。'))
    print(red(f'{str(e)} がありません。'))
    print(red('Failed to load config.json file. Make sure key name is correct. If this after update, plase check latest config.json file.'))
    print(red(f'{str(e)} is missing.'))
    dstore('ボット',f'>>> {traceback.format_exc()}')
    dstore('ボット',f'>>> config.json ファイルの読み込みに失敗しました。キーの名前が間違っていないか確認してください。アップデート後の場合は、最新のconfig.jsonファイルを確認してください。')
    dstore('ボット',f'>>> {str(e)} がありません')
    dstore('Bot',f'>>> Failed to load config.json file. Make sure key name is correct. If this after update, plase check latest config.json file.')
    dstore('Bot',f'>>> {str(e)} is missing.')
    sys.exit(1)
except json.decoder.JSONDecodeError as e:
    print(red(traceback.format_exc()))
    print(red(str(e)))
    print(red('config.json ファイルの読み込みに失敗しました。正しく書き込めているか確認してください。'))
    print(red('Failed to load config.json file. Make sure you wrote correctly.'))
    dstore('ボット',f'>>> {traceback.format_exc()}')
    dstore('ボット',f'>>> {str(e)}')
    dstore('ボット',f'>>> config.json ファイルの読み込みに失敗しました。正しく書き込めているか確認してください。')
    dstore('Bot',f'>>> Failed to load config.json file. Make sure you wrote correctly.')
    sys.exit(1)
except FileNotFoundError:
    print(red(traceback.format_exc()))
    print(red('config.json ファイルが存在しません。'))
    print(red('config.json file does not exist.'))
    dstore('ボット',f'>>> {traceback.format_exc()}')
    dstore('ボット',f'>>> config.json ファイルが存在しません。')
    dstore('Bot',f'>>> config.json file does not exist.')
    sys.exit(1)

if os.path.isfile(f"lang/{data['lang']}.json"):
    try:
        try:
            with open(f'lang/{data["lang"]}.json', 'r', encoding='utf-8') as f:
                localize = json.load(f)
        except json.decoder.JSONDecodeError:
            with open(f'lang/{data["lang"]}.json', 'r', encoding='utf-8-sig') as f:
                localize = json.load(f)
        if data['loglevel'] == 'debug':
            print(yellow(f'\n{localize}\n'))
            dstore('ボット',f'\n```\n{localize}\n```\n')
        for key in localizekeys:
            exec(f"errorcheck=localize['{key}']")
    except KeyError as e:
        print(red(traceback.format_exc()))
        print(red(f'{data["lang"]}.json ファイルの読み込みに失敗しました。キーの名前が間違っていないか確認してください。'))
        print(red(f'{str(e)} がありません。'))
        print(red(f'Failed to load {data["lang"]}.json file. Make sure key name is correct.'))
        print(red(f'{str(e)} is missing.'))
        dstore('ボット',f'>>> {traceback.format_exc()}')
        dstore('ボット',f'>>> {data["lang"]}.json ファイルの読み込みに失敗しました。キーの名前が間違っていないか確認してください。')
        dstore('ボット',f'>>> {str(e)} がありません')
        dstore('Bot',f'>>> Failed to load {data["lang"]}.json file. Make sure key name is correct.')
        dstore('Bot',f'>>> {str(e)} is missing.')
        sys.exit(1)
    except json.decoder.JSONDecodeError as e:
        print(red(traceback.format_exc()))
        print(red(f'{data["lang"]}.json ファイルの読み込みに失敗しました。正しく書き込めているか確認してください。'))
        print(red(str(e).replace('Expecting ','不明な',1).replace('Invalid control character at','無効なコントロール文字: ').replace('value','値',1).replace('delimiter','区切り文字',1).replace('line','行:',1).replace('column','文字:').replace('char ','',1)))
        print(red(f'Failed to load {data["lang"]}.json file. Make sure you wrote correctly.'))
        print(red(str(e)))
        dstore('ボット',f'>>> {traceback.format_exc()}')
        dstore('ボット',f'>>> {data["lang"]}.json ファイルの読み込みに失敗しました。正しく書き込めているか確認してください。')
        dstore('ボット',f'>>> {str(e).replace("Expecting ","不明な",1).replace("Invalid control character at","無効なコントロール文字: ").replace("value","値",1).replace("delimiter","区切り文字",1).replace("line","行:",1).replace("column","文字:").replace("char ","",1)}')
        dstore('Bot',f'>>> Failed to load {data["lang"]}.json file. Make sure you wrote correctly.')
        dstore('Bot',f'>>> {str(e)}')
        sys.exit(1)
    except FileNotFoundError:
        print(red(traceback.format_exc()))
        print(red(f'{data["lang"]}.json ファイルが存在しません。'))
        print(red(f'{data["lang"]}.json file does not exist.'))
        dstore('ボット',f'>>> {traceback.format_exc()}')
        dstore('ボット',f'>>> {data["lang"]}.json ファイルが存在しません。')
        dstore('Bot',f'>>> {data["lang"]}.json file does not exist.')
        sys.exit(1)
else:
    try:
        try:
            with open('lang/en.json', 'r', encoding='utf-8') as f:
                localize = json.load(f)
        except json.decoder.JSONDecodeError:
            with open('lang/en.json', 'r', encoding='utf-8-sig') as f:
                localize = json.load(f)
        if data['loglevel'] == 'debug':
            print(yellow(f'\n{localize}\n'))
            dstore('ボット',f'\n```\n{localize}\n```\n')
        for key in localizekeys:
            exec(f"errorcheck=localize['{key}']")
    except KeyError as e:
        print(red(traceback.format_exc()))
        print(red(f'en.json ファイルの読み込みに失敗しました。キーの名前が間違っていないか確認してください。'))
        print(red(f'{str(e)} がありません。'))
        print(red(f'Failed to load en.json file. Make sure key name is correct.'))
        print(red(f'{str(e)} is missing.'))
        dstore('ボット',f'>>> {traceback.format_exc()}')
        dstore('ボット',f'>>> en.json ファイルの読み込みに失敗しました。キーの名前が間違っていないか確認してください。')
        dstore('ボット',f'>>> {str(e)} がありません')
        dstore('Bot',f'>>> Failed to load en.json file. Make sure key name is correct.')
        dstore('Bot',f'>>> {str(e)} is missing.')
        sys.exit(1)
    except json.decoder.JSONDecodeError as e:
        print(red(traceback.format_exc()))
        print(red(str(e)))
        print(red(f'en.json ファイルの読み込みに失敗しました。正しく書き込めているか確認してください。'))
        print(red(f'Failed to load en.json file. Make sure you wrote correctly.'))
        dstore('ボット',f'>>> {traceback.format_exc()}')
        dstore('ボット',f'>>> {str(e)}')
        dstore('ボット',f'>>> en.json ファイルの読み込みに失敗しました。正しく書き込めているか確認してください。')
        dstore('Bot',f'>>> Failed to load en.json file. Make sure you wrote correctly.')
        sys.exit(1)
    except FileNotFoundError:
        print(red(traceback.format_exc()))
        print(red(f'en.json ファイルが存在しません。'))
        print(red(f'en.json file does not exist.'))
        dstore('ボット',f'>>> {traceback.format_exc()}')
        dstore('ボット',f'>>> en.json ファイルが存在しません。')
        dstore('Bot',f'>>> en.json file does not exist.')
        sys.exit(1)

try:
    try:
        with open('commands.json', 'r', encoding='utf-8') as f:
            commands=json.load(f)
    except json.decoder.JSONDecodeError:
        with open('commands.json', 'r', encoding='utf-8-sig') as f:
            commands=json.load(f)
    if data['loglevel'] == 'debug':
        print(yellow(f'\n{commands}\n'))
        dstore(l("bot"),f'\n```\n{commands}\n```\n')
    for key in commandskeys:
        exec(f"errorcheck=commands['{key}']")
    if data['caseinsensitive'] is True:
        commands=dict((k.lower(), jaconv.kata2hira(v.lower())) for k,v in commands.items())
    for checks in commands.items():
        if checks[0] in ignore:
            continue
        if commands['ownercommands'] == '':
            break
        for command in commands['ownercommands'].split(','):
            try:
                errorcheck=commands[command.lower()]
            except KeyError as e:
                print(red(traceback.format_exc()))
                print(red(l("failed_ownercommand")))
                print(red(l("is_missing", str(e))))
                dstore(l("bot"),f'>>> {traceback.format_exc()}')
                dstore(l("bot"),f'>>> {l("failed_ownercommand")}')
                dstore(l("bot"),f'>>> {l("is_missing", str(e))}')
                sys.exit(1)
except KeyError as e:
    print(red(traceback.format_exc()))
    print(red(l("load_failed_keyerror", "commands.json")))
    print(red(l("is_missing", str(e))))
    dstore(l("bot"),f'>>> {traceback.format_exc()}')
    dstore(l("bot"),f'>>> {l("load_failed_keyerror", "commands.json")}')
    dstore(l("bot"),f'>>> {l("is_missing", str(e))}')
    sys.exit(1)
except json.decoder.JSONDecodeError as e:
    print(red(traceback.format_exc()))
    print(red(str(e)))
    print(red(l("load_failed_json", "commands.json")))
    dstore(l("bot"),f'>>> {traceback.format_exc()}')
    dstore(l("bot"),f'>>> {str(e)}')
    dstore(l("bot"),f'>>> {l("load_failed_json", "commands.json")}')
    sys.exit(1)
except FileNotFoundError:
    print(red(traceback.format_exc()))
    print(red(l("load_failed_notfound", "commands.json")))
    dstore(l("bot"),f'>>> {traceback.format_exc()}')
    dstore(l("bot"),f'>>> {l("load_failed_notfound", "commands.json")}')
    sys.exit(1)

try:
    try:
        with open('replies.json', 'r', encoding='utf-8') as f:
            replies=json.load(f)
    except json.decoder.JSONDecodeError:
        with open('replies.json', 'r', encoding='utf-8-sig') as f:
            replies=json.load(f)
    if data['loglevel'] == 'debug':
        print(yellow(f'\n{replies}\n'))
        dstore(l("bot"),f'\n```\n{replies}\n```\n')
    if data['caseinsensitive'] is True:
        replies=dict((jaconv.kata2hira(k.lower()), v) for k,v in replies.items())
except json.decoder.JSONDecodeError as e:
    print(red(traceback.format_exc()))
    print(red(str(e)))
    print(red(l("load_failed_json", "replies.json")))
    dstore(l("bot"),f'>>> {traceback.format_exc()}')
    dstore(l("bot"),f'>>> {str(e)}')
    dstore(l("bot"),f'>>> {l("load_failed_json", "replies.json")}')
    sys.exit(1)
except FileNotFoundError:
    print(red(traceback.format_exc()))
    print(red(l("load_failed_notfound", "replies.json")))
    dstore(l("bot"),f'>>> {traceback.format_exc()}')
    dstore(l("bot"),f'>>> {l("load_failed_notfound", "replies.json")}')
    sys.exit(1)

threading.Thread(target=dprint,args=()).start()
threading.Thread(target=get_item_info,args=()).start()

if data['debug'] is True:
    logger = logging.getLogger('fortnitepy.http')
    logger.setLevel(level=logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter('\u001b[36m %(asctime)s:%(levelname)s:%(name)s: %(message)s \u001b[0m'))
    logger.addHandler(handler)

    logger = logging.getLogger('fortnitepy.xmpp')
    logger.setLevel(level=logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter('\u001b[35m %(asctime)s:%(levelname)s:%(name)s: %(message)s \u001b[0m'))
    logger.addHandler(handler)

if True:
    if data['fortnite']['whisper'] not in (True, False):
        data['fortnite']['whisper'] = True
    if data['fortnite']['partychat'] not in (True, False):
        data['fortnite']['partychat'] = True
    if data['fortnite']['disablewhisperperfectly'] not in (True, False):
        data['fortnite']['disablewhisperperfectly'] = False
    if data['fortnite']['disablepartychatperfectly'] not in (True, False):
        data['fortnite']['disablepartychatperfectly'] = False
    if data['fortnite']['joinmessageenable'] not in (True, False):
        data['fortnite']['joinmessageenable'] = False
    if data['fortnite']['randommessageenable'] not in (True, False):
        data['fortnite']['randommessageenable'] = False
    if data['fortnite']['outfitmimic'] not in (True, False):
        data['fortnite']['outfitmimic'] = False
    if data['fortnite']['backpackmimic'] not in (True, False):
        data['fortnite']['backpackmimic'] = False
    if data['fortnite']['pickaxemimic'] not in (True, False):
        data['fortnite']['pickaxemimic'] = False
    if data['fortnite']['emotemimic'] not in (True, False):
        data['fortnite']['emotemimic'] = False
    if data['fortnite']['acceptinvite'] not in (True, False):
        data['fortnite']['acceptinvite'] = True
    if data['fortnite']['acceptfriend'] not in (True, False, None):
        data['fortnite']['acceptfriend'] = True
    if data['fortnite']['addfriend'] not in (True, False):
        data['fortnite']['addfriend'] = False
    if data['fortnite']['invite-ownerdecline'] not in (True, False):
        data['fortnite']['invite-ownerdecline'] = False
    if data['fortnite']['inviteinterval'] not in (True, False):
        data['fortnite']['inviteinterval'] = False
    if data['fortnite']['blacklist-declineinvite'] not in (True, False):
        data['fortnite']['blacklist-declineinvite'] = False
    if data['fortnite']['blacklist-autoblock'] not in (True, False):
        data['fortnite']['blacklist-autoblock'] = False
    if data['fortnite']['blacklist-autokick'] not in (True, False):
        data['fortnite']['blacklist-autokick'] = False
    if data['fortnite']['blacklist-autochatban'] not in (True, False):
        data['fortnite']['blacklist-autochatban'] = False
    if data['fortnite']['blacklist-ignorecommand'] not in (True, False):
        data['fortnite']['blacklist-ignorecommand'] = False
    if data['fortnite']['whitelist-allowinvite'] not in (True, False):
        data['fortnite']['whitelist-allowinvite'] = False
    if data['fortnite']['whitelist-declineinvite'] not in (True, False):
        data['fortnite']['whitelist-declineinvite'] = False
    if data['fortnite']['whitelist-ignorelock'] not in (True, False):
        data['fortnite']['whitelist-ignorelock'] = False
    if data['fortnite']['whitelist-ownercommand'] not in (True, False):
        data['fortnite']['whitelist-ownercommand'] = False

if True:
    if data['discord']['enabled'] not in (True, False):
        data['discord']['enabled'] = False
    if data['discord']['discord'] not in (True, False):
        data['discord']['discord'] = True
    if data['discord']['disablediscordperfectly'] not in (True, False):
        data['discord']['disablediscordperfectly'] = True
    if data['discord']['blacklist-ignorecommand'] not in (True, False):
        data['discord']['blacklist-ignorecommand'] = False
    if data['discord']['whitelist-ignorelock'] not in (True, False):
        data['discord']['whitelist-ignorelock'] = False
    if data['discord']['whitelist-ownercommand'] not in (True, False):
        data['discord']['whitelist-ownercommand'] = False

if True:
    if data['no-logs'] not in (True, False):
        data['no-logs'] = False
    if data['ingame-error'] not in (True, False):
        data['ingame-error'] = True
    if data['discord-log'] not in (True, False):
        data['discord-log'] = False
    if data['hide-email'] not in (True, False):
        data['hide-email'] = True
    if data['hide-password'] not in (True, False):
        data['hide-password'] = True
    if data['hide-webhook'] not in (True, False):
        data['hide-webhook'] = True
    if data['caseinsensitive'] not in (True, False):
        data['caseinsensitive'] = True
    if data['loglevel'] not in ('normal', 'info', 'debug'):
        data['loglevel'] = 'normal'
    if data['fortnite']['privacy'] not in ('public', 'friends_allow_friends_of_friends', 'friends', 'private_allow_friends_of_friends', 'private'):
        data['fortnite']['privacy'] = 'public'

data['fortnite']['privacy']=eval(f"fortnitepy.PartyPrivacy.{data['fortnite']['privacy'].upper()}")

print(cyan(f'{l("lobbybot")}: gomashio\n{l("credit")}\n{l("library")}: Terbau'))
dstore(l("bot"),f'{l("lobbybot")}: gomashio\n{l("credit")}\n{l("library")}: Terbau')
if True:
    if data['loglevel'] == 'normal':
        print(green(f'\n{l("loglevel")}: {l("normal")}'))
        dstore(l("bot"),f'\n{l("loglevel")}: {l("normal")}')
    elif data['loglevel'] == 'info':
        print(green(f'\n{l("loglevel")}: {l("info")}'))
        dstore(l("bot"),f'\n{l("loglevel")}: {l("info")}')
    elif data['loglevel'] == 'debug':
        print(green(f'\n{l("loglevel")}: {l("debug")}'))
        dstore(l("bot"),f'\n{l("loglevel")}: {l("debug")}')
    if data['debug'] is True:
        print(green(f'{l("debug")}: {l("on")}'))
        dstore(l("bot"),f'{l("debug")}: {l("on")}')
    else:
        print(green(f'{l("debug")}: {l("off")}'))
        dstore(l("bot"),f'{l("debug")}: {l("off")}')
print(green(f'\nPython {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'))
print(green(f'Fortnitepy {fortnitepy.__version__}'))
print(green(f'discord.py {discord.__version__}'))
if data['debug'] is True:
    print(red(f'[{now_()}] {l("debug_is_on")}'))
    dstore(l("bot"),f'>>> {l("debug_is_on")}')
if data['no-logs'] is False:
    print(l("booting"))
dstore(l("bot"),l("booting"))

async def event_device_auth_generate(details: dict, email: str) -> None:
    store_device_auth_details(email, details)

async def event_ready(client: fortnitepy.Client) -> None:
    global blacklist_flag
    global blacklist
    global whitelist_flag
    global whitelist
    global invitelist_flag
    global otherbotlist
    global otherbotlist_flag
    global discord_flag
    global client_name
    global loadedclients
    if data['loglevel'] == 'normal':
        if data['no-logs'] is False:
            print(green(f'[{now_()}] {l("login")}: {client.user.display_name}'))
        dstore(client.user.display_name,f'{l("login")}: {client.user.display_name}')
    else:
        if data['no-logs'] is False:
            print(green(f'[{now_()}] {l("login")}: {client.user.display_name} / {client.user.id}'))
        dstore(client.user.display_name,f'{l("login")}: {client.user.display_name} / {client.user.id}')
    client.isready=True
    loadedclients.append(client)
    client_name[client.user.display_name] = client
    add_cache(client, client.user)
    for friend_ in client.friends.values():
        add_cache(client, friend_)
    for pending_ in client.pending_friends.values():
        add_cache(client, pending_)
    for block_ in client.blocked_users.values():
        add_cache(client, block_)

    try:
        client.owner=None
        owner=await client.fetch_profile(data['fortnite']['owner'])
        if owner is None:
            print(red(f'[{now_()}] [{client.user.display_name}] {l("owner_notfound")}'))
            dstore(client.user.display_name,f'>>> {l("owner_notfound")}')
        else:
            add_cache(client, owner)
            client.owner=client.get_friend(owner.id)
            if client.owner is None:
                if data['fortnite']['addfriend'] is True:
                    try:
                        await client.add_friend(owner.id)
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                        if data['loglevel'] == 'normal':
                            print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_sending_friendrequest")}'))
                            dstore(client.user.display_name,f'>>> {l("error_while_sending_friendrequest")}')
                        else:
                            print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_sending_friendrequest")}'))
                            dstore(client.user.display_name,f'>>> {l("error_while_sending_friendrequest")}')
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] {l("not_friend_with_owner", commands["reload"])}'))
                dstore(client.user.display_name,f'>>> {l("not_friend_with_owner", commands["reload"])}')
            else:
                if data['loglevel'] == 'normal':
                    if data['no-logs'] is False:
                        print(green(f'[{now_()}] [{client.user.display_name}] {l("owner")}: {str(client.owner.display_name)}'))
                    dstore(client.user.display_name,f'{l("owner")}: {str(client.owner.display_name)}')
                else:
                    if data['no-logs'] is False:
                        print(green(f'[{now_()}] [{client.user.display_name}] {l("owner")}: {str(client.owner.display_name)} / {client.owner.id}'))
                    dstore(client.user.display_name,f'{l("owner")}: {str(client.owner.display_name)} / {client.owner.id}')
    except fortnitepy.HTTPException:
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
        dstore(client.user.display_name,f'>>> {l("error_while_requesting_userinfo")}')
    except Exception:
        print(red(traceback.format_exc()))
        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    
    if client.owner is not None:
        await client.owner.send(l("click_invite"))

    if blacklist_flag is True:
        blacklist_flag = False
        for blacklistuser in data['fortnite']['blacklist']:
            try:
                user = await client.fetch_profile(blacklistuser)
                add_cache(client, user)
                if user is None:
                    print(red(f'[{now_()}] [{client.user.display_name}] {l("blacklist_user_notfount", blacklistuser)}'))
                    dstore(client.user.display_name,f'>>> {l("blacklist_user_notfount", blacklistuser)}')
                else:
                    blacklist.append(user.id)
                    if data['loglevel'] == 'debug':
                        print(yellow(f"{str(user.display_name)} / {user.id}"))
                    if data['fortnite']['blacklist-autoblock'] is True:
                        try:
                            await user.block()
                        except Exception:
                            if data['loglevel'] == 'debug':
                                print(red(traceback.format_exc()))
                                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
                dstore(client.user.display_name,f'>>> {l("error_while_requesting_userinfo")}')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        if data['loglevel'] == "debug":
            print(yellow(blacklist))
    if whitelist_flag is True:
        whitelist_flag = False
        for whitelistuser in data['fortnite']['whitelist']:
            try:
                user = await client.fetch_profile(whitelistuser)
                add_cache(client, user)
                if user is None:
                    print(red(f'[{now_()}] [{client.user.display_name}] {l("whitelist_user_notfound", whitelistuser)}'))
                    dstore(client.user.display_name,f'>>> {l("whitelist_user_notfound", whitelistuser)}')
                else:
                    whitelist.append(user.id)
                    if data['loglevel'] == 'debug':
                        print(yellow(f"{str(user.display_name)} / {user.id}"))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
                dstore(client.user.display_name,f'>>> {l("error_while_requesting_userinfo")}')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        if data['loglevel'] == "debug":
            print(yellow(whitelist))

    if otherbotlist_flag is True:
        otherbotlist_flag = False
        for otherbotlistuser in data['fortnite']['otherbotlist']:
            try:
                user = await client.fetch_profile(otherbotlistuser)
                add_cache(client, user)
                if user is None:
                    print(red(f'[{now_()}] [{client.user.display_name}] {l("botlist_user_notfound", otherbotlistuser)}'))
                    dstore(client.user.display_name,f'>>> {l("botlist_user_notfound", otherbotlistuser)}')
                else:
                    otherbotlist.append(user.id)
                    if data['loglevel'] == 'debug':
                        print(yellow(f"{str(user.display_name)} / {user.id}"))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
                dstore(client.user.display_name,f'>>> {l("error_while_requesting_userinfo")}')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        if data['loglevel'] == "debug":
            print(yellow(otherbotlist))

    for invitelistuser in data['fortnite']['invitelist']:
        try:
            user = await client.fetch_profile(invitelistuser)
            if user is None:
                print(red(f'[{now_()}] [{client.user.display_name}] {l("invitelist_user_notfound")}'))
                dstore(client.user.display_name,f'>>> {l("invitelist_user_notfound")}')
            else:
                friend = client.get_friend(user.id)
                if friend is None and user.id != client.user.id:
                    if data['fortnite']['addfriend'] is True:
                        try:
                            await client.add_friend(friend.id)
                        except fortnitepy.HTTPException:
                            if data['loglevel'] == 'debug':
                                print(red(traceback.format_exc()))
                                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                            if data['loglevel'] == 'normal':
                                print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_sending_friendrequest")}'))
                                dstore(client.user.display_name,f'>>> {l("error_while_sending_friendrequest")}')
                            else:
                                print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_sending_friendrequest")}'))
                            dstore(client.user.display_name,f'>>> {l("error_while_sending_friendrequest")}')
                        except Exception:
                            print(red(traceback.format_exc()))
                            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                    print(red(f'[{now_()}] [{client.user.display_name}] {l("not_friend_with_inviteuser", invitelistuser, commands["reload"])}'))
                    dstore(client.user.display_name,f'>>> {l("not_friend_with_inviteuser", invitelistuser, commands["reload"])}')
                else:
                    add_cache(client, user)
                    client.invitelist.append(user.id)
                    if data['loglevel'] == 'debug':
                        print(yellow(f"{str(user.display_name)} / {user.id}"))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
            dstore(client.user.display_name,f'>>> {l("error_while_requesting_userinfo")}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    if data['loglevel'] == "debug":
        print(yellow(client.invitelist))

    if data['fortnite']['acceptfriend'] is True:
        pendings=[]
        for pending in client.pending_friends.copy().values():
            add_cache(client, pending)
            if pending.direction == 'INBOUND':
                pendings.append(pending)
        for pending in pendings:
            if client.acceptfriend is True:
                try:
                    await pending.accept()
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                    try:
                        await pending.decline()
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            else:
                try:
                    await pending.decline()
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    
    if data['discord']['enabled'] is True and discord_flag is True:
        discord_flag = False
        await dclient.start(data['discord']['token'])

async def event_restart() -> None:
    if data['no-logs'] is False:
        print(green(f'[{now_()}] {l("relogin")}'))
    dstore(l("bot"),f'>>> {l("relogin")}')

async def event_party_invite(invitation: fortnitepy.ReceivedPartyInvitation) -> None:
    global blacklist
    global whitelist
    if invitation is None:
        return
    client=invitation.client
    if client.isready is False:
        return
    add_cache(client, invitation.sender)
    if invitation.sender.id in blacklist:
        if data['fortnite']['blacklist-declineinvite'] is True:
            try:
                await invitation.decline()
            except Exception:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            return
    if client.owner is not None:
        if invitation.sender.id == client.owner.id:
            await invitation_accept(invitation)
            return
        elif invitation.sender.id in whitelist and data['fortnite']['whitelist-allowinvite'] is True:
            await invitation_accept(invitation)
            return
    else:
        if invitation.sender.id in whitelist and data['fortnite']['whitelist-allowinvite'] is True:
            await invitation_accept(invitation)
            return
    if data['loglevel'] == 'normal':
        if data['no-logs'] is False:
            print(f'[{now_()}] [{client.user.display_name}] {l("invite_from", str(invitation.sender.display_name))}')
        dstore(client.user.display_name,l("invite_from", str(invitation.sender.display_name)))
    else:
        if data['no-logs'] is False:
            print(f'[{now_()}] [{client.user.display_name}] {l("invite_from2", f"{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}]", invitation.party.id)}')
        dstore(client.user.display_name,l("invite_from2", f"{str(invitation.sender.display_name)} / {invitation.sender.id} [{platform_to_str(invitation.sender.platform)}]", invitation.party.id))

    if client.owner is not None:
        if client.owner.id in client.party.members.keys() and data['fortnite']['invite-ownerdecline'] is True:
            await invitation_decline_owner(invitation)
            return
    if True in [memberid in whitelist for memberid in client.party.members.keys()] and data['fortnite']['whitelist-declineinvite'] is True:
        await invitation_decline_whitelist(invitation)
    elif client.acceptinvite is False:
        await invitation_decline(invitation)
    elif client.acceptinvite_interval is False:
        await invitation_decline_interval(invitation)
    else:
        await invitation_accept(invitation)

async def event_friend_request(request: fortnitepy.PendingFriend) -> None:
    if request is None:
        return
    client=request.client
    if client.isready is False:
        return
    add_cache(client, request)
    if request.direction == 'OUTBOUND':
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(f'[{now_()}] [{client.user.display_name}] {l("friend_request_to", str(request.display_name))}')
            dstore(client.user.display_name,l("friend_request_to", str(request.display_name)))
        else:
            if data['no-logs'] is False:
                print(f'[{now_()}] [{client.user.display_name}] {l("friend_request_to", f"{str(request.display_name)} / {request.id}")}')
            dstore(client.user.display_name,l("friend_request_to", f"{str(request.display_name)} / {request.id}"))
        return
    if data['loglevel'] == 'normal':
        if data['no-logs'] is False:
            print(f'[{now_()}] [{client.user.display_name}] {l("friend_request_from", str(request.display_name))}')
        dstore(client.user.display_name,l("friend_request_from", str(request.display_name)))
    else:
        if data['no-logs'] is False:
            print(f'[{now_()}] [{client.user.display_name}] {l("friend_request_from", f"{str(request.display_name)} / {request.id}")}')
        dstore(client.user.display_name,l("friend_request_from", f"{str(request.display_name)} / {request.id}"))
    if client.acceptfriend is True:
        try:
            await request.accept()
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            if data['loglevel'] == 'normal':
                print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_accepting_friendrequest")}'))
                dstore(client.user.display_name,f'>>> {l("error_while_accepting_friendrequest")}')
            else:
                print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_accepting_friendrequest")}'))
                dstore(client.user.display_name,f'>>> {l("error_while_accepting_friendrequest")}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    elif client.acceptfriend is False:
        try:
            await request.decline()
            if data['loglevel'] == 'normal':
                if data['no-logs'] is False:
                    print(f'[{now_()}] [{client.user.display_name}] {l("friend_request_decline", str(request.display_name))}')
                dstore(client.user.display_name,l("friend_request_decline", str(request.display_name)))
            else:
                if data['no-logs'] is False:
                    print(f'[{now_()}] [{client.user.display_name}] {l("friend_request_decline", f"{str(request.display_name)} / {request.id}")}')
                dstore(client.user.display_name,l("friend_request_decline", f"{str(request.display_name)} / {request.id}"))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            if data['loglevel'] == 'normal':
                print(f'[{now_()}] [{client.user.display_name}] {l("error_while_declining_friendrequest")}')
                dstore(client.user.display_name,f'>>> {l("error_while_declining_friendrequest")}')
            else:
                print(f'[{now_()}] [{client.user.display_name}] {l("error_while_declining_friendrequest")}')
                dstore(client.user.display_name,f'>>> {l("error_while_declining_friendrequest")}')
        except Exception:
            print(red(traceback.format_exc()))

async def event_friend_add(friend: fortnitepy.Friend) -> None:
    if friend is None:
        return
    client=friend.client
    if client.isready is False:
        return
    add_cache(client, friend)
    if friend.direction == 'OUTBOUND':
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(f'[{now_()}] [{client.user.display_name}] {l("friend_accept", str(friend.display_name))}')
            dstore(client.user.display_name,l("friend_accept", str(friend.display_name)))
        else:
            if data['no-logs'] is False:
                print(f'[{now_()}] [{client.user.display_name}] {l("friend_accept", f"{str(friend.display_name)} / {friend.id}")}')
            dstore(client.user.display_name,l("friend_accept", f"{str(friend.display_name)} / {friend.id}"))
    else:
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(f'[{now_()}] [{client.user.display_name}] {l("friend_add", str(friend.display_name))}')
            dstore(client.user.display_name,l("friend_add", str(friend.display_name)))
        else:
            if data['no-logs'] is False:
                print(f'[{now_()}] [{client.user.display_name}] {l("friend_add", f"{str(friend.display_name)} / {friend.id}")}')
            dstore(client.user.display_name,l("friend_add", f"{str(friend.display_name)} / {friend.id}"))

async def event_friend_remove(friend: fortnitepy.Friend) -> None:
    if friend is None:
        return
    client=friend.client
    if client.isready is False:
        return
    add_cache(client, friend)
    if data['loglevel'] == 'normal':
        if data['no-logs'] is False:
            print(f'[{now_()}] [{client.user.display_name}] {l("friend_remove", str(friend.display_name))}')
        dstore(client.user.display_name,l("friend_remove", str(friend.display_name)))
    else:
        if data['no-logs'] is False:
            print(f'[{now_()}] [{client.user.display_name}] {l("friend_remove", f"{str(friend.display_name)} / {friend.id} [{platform_to_str(friend.platform)}]")}')
        dstore(client.user.display_name,l("friend_remove", f"{str(friend.display_name)} / {friend.id} [{platform_to_str(friend.platform)}]"))

async def event_party_member_join(member: fortnitepy.PartyMember) -> None:
    global blacklist
    if member is None:
        return
    client=member.client
    if client.isready is False:
        return
    add_cache(client, member)
    client_user_display_name=str(client.user.display_name)
    member_joined_at_most=[]
    for member_ in client.party.members.values():
        add_cache(client, member_)
        try:
            if member_joined_at_most != []:
                if member_.id in [i.user.id for i in loadedclients]:
                    if member_.id != client.user.id:
                        client_user_display_name+=f"/{str(member_.display_name)}"
                    if member_.joined_at < member_joined_at_most[1]:
                        member_joined_at_most=[member_.id, member_.joined_at]
            else:
                member_joined_at_most=[client.user.id, client.party.me.joined_at]
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    if member_joined_at_most == []:
        member_joined_at_most=[client.user.id]
    if client.user.id == member_joined_at_most[0]:
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [{l("party")}] [{client_user_display_name}] {l("party_member_joined", str(member.display_name), member.party.member_count)}'))
            dstore(client_user_display_name,f'[{l("party")}] {l("party_member_joined", str(member.display_name), member.party.member_count)}')
        else:
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [{l("party")}/{client.party.id}] [{client_user_display_name}] {l("party_member_joined", f"{str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}]", member.party.member_count)}'))
            dstore(client_user_display_name,f'[{l("party")}/{client.party.id}] {l("party_member_joined", f"{str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}]", member.party.member_count)}')
    
    if member.id in blacklist and client.party.me.leader is True:
        if data['fortnite']['blacklist-autokick'] is True:
            try:
                await member.kick()
            except Exception:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            return
        if data['fortnite']['blacklist-autochatban'] is True:
            try:
                await member.chatban()
            except Exception:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            return
    
    if data['fortnite']['addfriend'] is True:
        for member in member.party.members.keys():
            try:
                await client.add_friend(member)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            except Exception:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

    await asyncio.sleep(0.1)

    if client.joinmessageenable is True:
        try:
            await client.party.send(data['fortnite']['joinmessage'])
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    if client.randommessageenable is True:
        try:
            randommessage=random.choice(data['fortnite']['randommessage'].split(','))
            if data['no-logs'] is False:
                print(f'[{now_()}] [{client.user.display_name}] {l("random_message")}: {randommessage}')
            dstore(client.user.display_name,f'{l("random_message")}: {randommessage}')
            await client.party.send(randommessage)
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')


    try:
        await change_asset(client, client.user.id, "emote", client.eid)
    except Exception:
        if data['loglevel'] == 'debug':
            print(red(traceback.format_exc()))
            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

    if client.party.leader.id == client.user.id:
        try:
            await client.party.set_playlist(data['fortnite']['playlist'])
            await client.party.set_privacy(data['fortnite']['privacy'])
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

async def event_party_member_leave(member: fortnitepy.PartyMember) -> None:
    if member is None:
        return
    client=member.client
    if client.isready is False:
        return
    add_cache(client, member)
    client_user_display_name=str(client.user.display_name)
    member_joined_at_most=[]
    for member_ in client.party.members.values():
        add_cache(client, member_)
        try:
            if member_joined_at_most != []:
                if member_.id in [i.user.id for i in loadedclients]:
                    if member_.id != client.user.id:
                        client_user_display_name+=f"/{str(member_.display_name)}"
                    if member_.joined_at < member_joined_at_most[1]:
                        member_joined_at_most=[member_.id, member_.joined_at]
            else:
                member_joined_at_most=[client.user.id, client.party.me.joined_at]
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    if member_joined_at_most == []:
        member_joined_at_most=[client.user.id]
    if client.user.id == member_joined_at_most[0]:
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [{l("party")}] [{client_user_display_name}] {l("party_member_left", str(member.display_name), member.party.member_count)}'))
            dstore(client_user_display_name,f'[{l("party")}] {l("party_member_left", str(member.display_name), member.party.member_count)}')
        else:
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [{l("party")}/{client.party.id}] [{client_user_display_name}] {l("party_member_left", f"{str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}]", member.party.member_count)}'))
            dstore(client_user_display_name,f'[{l("party")}/{client.party.id}] {l("party_member_left", f"{str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}]", member.party.member_count)}')

    if data['fortnite']['addfriend'] is True:
        for member in member.party.members.keys():
            try:
                await client.add_friend(member)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                continue
            except Exception:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

async def event_party_member_confirm(confirmation: fortnitepy.PartyJoinConfirmation) -> None:
    global blacklist
    if confirmation is None:
        return
    client=confirmation.client
    if client.isready is False:
        return
    add_cache(client, confirmation.user)
    if data['loglevel'] != 'normal':
        if data['no-logs'] is False:
            print(magenta(f'[{now_()}] [{l("party")}/{client.party.id}] [{client.user.display_name}] {l("party_member_request", f"{str(confirmation.user.display_name)} / {confirmation.user.id}")}'))
        dstore(client.user.display_name,f'[{l("party")}/{client.party.id}] {l("party_member_request", f"{str(confirmation.user.display_name)} / {confirmation.user.id}")}')
            
    if data['fortnite']['blacklist-autokick'] is True and confirmation.user.id in blacklist:
        try:
            await confirmation.reject()
        except fortnitepy.HTTPException:
            if data['loglevel'] == "debug":
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            print(red(l("error_while_declining_partyrequest")))
    else:
        try:
            await confirmation.confirm()
        except fortnitepy.HTTPException:
            if data['loglevel'] == "debug":
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            print(red(l("error_while_declining_partyrequest")))

async def event_party_member_kick(member: fortnitepy.PartyMember) -> None:
    if member is None:
        return
    client=member.client
    if client.isready is False:
        return
    add_cache(client, member)
    client_user_display_name=str(client.user.display_name)
    member_joined_at_most=[]
    for member_ in client.party.members.values():
        add_cache(client, member_)
        try:
            if member_joined_at_most != []:
                if member_.id in [i.user.id for i in loadedclients]:
                    if member_.id != client.user.id:
                        client_user_display_name+=f"/{str(member_.display_name)}"
                    if member_.joined_at < member_joined_at_most[1]:
                        member_joined_at_most=[member_.id, member_.joined_at]
            else:
                member_joined_at_most=[client.user.id, client.party.me.joined_at]
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    if member_joined_at_most == []:
        member_joined_at_most=[client.user.id]
    if client.user.id == member_joined_at_most[0]:
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [{l("party")}] [{client_user_display_name}] {l("party_member_kick", str(member.party.leader.display_name), str(member.display_name), member.party.member_count)}'))
            dstore(client_user_display_name,f'[{l("party")}] {l("party_member_kick", str(member.party.leader.display_name), str(member.display_name), member.party.member_count)}')
        else:
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [{l("party")}/{client.party.id}] [{client_user_display_name}] {l("party_member_kick", f"{str(member.party.leader.display_name)} / {member.party.leader.id} [{platform_to_str(member.party.leader.platform)}/{member.input}]", f"{str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}]", member.party.member_count)}'))
            dstore(client_user_display_name,f'[{l("party")}/{client.party.id}] {l("party_member_kick", f"{str(member.party.leader.display_name)} / {member.party.leader.id} [{platform_to_str(member.party.leader.platform)}/{member.input}]", f"{str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}]", member.party.member_count)}')

async def event_party_member_promote(old_leader: fortnitepy.PartyMember, new_leader: fortnitepy.PartyMember) -> None:
    global blacklist
    if old_leader is None or new_leader is None:
        return
    client=new_leader.client
    if client.isready is False:
        return
    client_user_display_name=str(client.user.display_name)
    member_joined_at_most=[]
    for member_ in client.party.members.values():
        add_cache(client, member_)
        try:
            if member_joined_at_most != []:
                if member_.id in [i.user.id for i in loadedclients]:
                    if member_.id != client.user.id:
                        client_user_display_name+=f"/{str(member_.display_name)}"
                    if member_.joined_at < member_joined_at_most[1]:
                        member_joined_at_most=[member_.id, member_.joined_at]
            else:
                member_joined_at_most=[client.user.id, client.party.me.joined_at]
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    if member_joined_at_most == []:
        member_joined_at_most=[client.user.id]
    if client.user.id == member_joined_at_most[0]:
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [{l("party")}] [{client_user_display_name}] {l("party_member_promote", str(old_leader.display_name), str(new_leader.display_name))}'))
            dstore(client_user_display_name,f'[{l("party")}] {l("party_member_promote", str(old_leader.display_name), str(new_leader.display_name))}')
        else:
            if data['no-logs'] is False:

                print(magenta(f'[{now_()}] [{l("party")}/{client.party.id}] [{client_user_display_name}] {l("party_member_promote", f"{str(old_leader.display_name)} / {old_leader.id} [{platform_to_str(old_leader.platform)}/{old_leader.input}]", f"{str(new_leader.display_name)} / {new_leader.id} [{platform_to_str(new_leader.platform)}/{new_leader.input}]")}'))
            dstore(client_user_display_name,f'[{l("party")}/{client.party.id}] {l("party_member_promote", f"{str(old_leader.display_name)} / {old_leader.id} [{platform_to_str(old_leader.platform)}/{old_leader.input}]", f"{str(new_leader.display_name)} / {new_leader.id} [{platform_to_str(new_leader.platform)}/{new_leader.input}]")}')
    
    if new_leader.id == client.user.id:
        try:
            await client.party.set_playlist(data['fortnite']['playlist'])
            await client.party.set_privacy(data['fortnite']['privacy'])
            for member in client.party.members.values():
                if member.id in blacklist:
                    if data['fortnite']['blacklist-autokick'] is True:
                        try:
                            await member.kick()
                        except Exception:
                            if data['loglevel'] == 'debug':
                                print(red(traceback.format_exc()))
                                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                    if data['fortnite']['blacklist-autochatban'] is True:
                        try:
                            await member.chatban()
                        except Exception:
                            if data['loglevel'] == 'debug':
                                print(red(traceback.format_exc()))
                                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

async def event_party_member_update(member: fortnitepy.PartyMember) -> None:
    global blacklist
    if member is None:
        return
    client=member.client
    if client.isready is False:
        return
    client_user_display_name=str(client.user.display_name)
    member_joined_at_most=[]
    for member_ in client.party.members.values():
        add_cache(client, member_)
        try:
            if member_joined_at_most != []:
                if member_.id in [i.user.id for i in loadedclients]:
                    if member_.id != client.user.id:
                        client_user_display_name+=f"/{str(member_.display_name)}"
                    if member_.joined_at < member_joined_at_most[1]:
                        member_joined_at_most=[member_.id, member_.joined_at]
            else:
                member_joined_at_most=[client.user.id, client.party.me.joined_at]
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    if member_joined_at_most == []:
        member_joined_at_most=[client.user.id]
    if client.user.id == member_joined_at_most[0]:
        if data['loglevel'] != 'normal':
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [{l("party")}/{client.party.id}] [{client_user_display_name}] {l("party_member_update", f"{str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}]")}'))
            dstore(client_user_display_name,f'[{l("party")}/{client.party.id}] {l("party_member_update", f"{str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}]")}')
    
    if member.id == client.user.id:
        return
    if member.id in blacklist and client.party.me.leader is True:
        if data['fortnite']['blacklist-autokick'] is True:
            try:
                await member.kick()
            except Exception:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            return
        if data['fortnite']['blacklist-autochatban'] is True:
            try:
                await member.chatban()
            except Exception:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            return
    if member.outfit != client.prevoutfit or member.outfit_variants != client.prevoutfitvariants or member.enlightenments != client.prevenlightenments:
        if data['loglevel'] != 'normal':
            if client.user.id == member_joined_at_most[0]:
                if data['no-logs'] is False:
                    print(str(member.outfit))
                dstore(client_user_display_name,str(member.outfit))
        if client.outfitmimic is True:
            if member.outfit is None:
                try:
                    await change_asset(client, client.user.id, "outfit", "")
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            else:
                try:
                    await change_asset(client, client.user.id, "outfit", member.outfit, member.outfit_variants, member.enlightenments)
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    if partymember_backpack(member) != client.prevbackpack or member.backpack_variants != client.prevbackpackvariants:
        if data['loglevel'] != 'normal':
            if client.user.id == member_joined_at_most[0]:
                if data['no-logs'] is False:
                    print(str(partymember_backpack(member)))
                dstore(client_user_display_name,str(partymember_backpack(member)))
        if client.backpackmimic is True:
            if partymember_backpack(member) is None:
                try:
                    await change_asset(client, client.user.id, "backpack", "")
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            else:
                try:
                    type_ = convert_to_type(partymember_backpack(member))
                    await change_asset(client, client.user.id, type_, partymember_backpack(member), member.backpack_variants)
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    if member.pickaxe != client.prevpickaxe or member.pickaxe_variants != client.prevpickaxevariants:
        if data['loglevel'] != 'normal':
            if client.user.id == member_joined_at_most[0]:
                if data['no-logs'] is False:
                    print(str(member.pickaxe))
                dstore(client_user_display_name,str(member.pickaxe))
        if client.pickaxemimic is True:
            if member.pickaxe is None:
                try:
                    await change_asset(client, client.user.id, "pickaxe", "")
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            else:
                try:
                    await change_asset(client, client.user.id, "pickaxe", member.pickaxe, member.pickaxe_variants)
                except Exception:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    client.prevoutfit=member.outfit
    client.prevoutfitvariants=member.outfit_variants
    client.prevenlightenments=member.enlightenments
    client.prevbackpack=partymember_backpack(member)
    client.prevbackpackvariants=member.backpack_variants
    client.prevpickaxe=member.pickaxe
    client.prevpickaxevariants=member.pickaxe_variants

    if partymember_emote(member) is not None:
        if data['loglevel'] != 'normal':
            if client.user.id == member_joined_at_most[0]:
                if data['no-logs'] is False:
                    print(str(partymember_emote(member)))
                dstore(client_user_display_name,str(partymember_emote(member)))
        if client.emotemimic is True:
            try:
                await change_asset(client, client.user.id, "emote", partymember_emote(member))
            except Exception:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

async def event_party_member_disconnect(member: fortnitepy.PartyMember) -> None:
    if member is None:
        return
    client=member.client
    if client.isready is False:
        return
    add_cache(client, member)
    client_user_display_name=str(client.user.display_name)
    member_joined_at_most=[]
    for member_ in client.party.members.values():
        add_cache(client, member_)
        try:
            if member_joined_at_most != []:
                if member_.id in [i.user.id for i in loadedclients]:
                    if member_.id != client.user.id:
                        client_user_display_name+=f"/{str(member_.display_name)}"
                    if member_.joined_at < member_joined_at_most[1]:
                        member_joined_at_most=[member_.id, member_.joined_at]
            else:
                member_joined_at_most=[client.user.id, client.party.me.joined_at]
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    if member_joined_at_most == []:
        member_joined_at_most=[client.user.id]
    if client.user.id == member_joined_at_most[0]:
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [{l("party")}] [{client_user_display_name}] {l("party_member_disconnect", str(member.display_name))}'))
            dstore(client_user_display_name,f'[{l("party")}] {l("party_member_disconnect", str(member.display_name))}')
        else:
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [{l("party")}/{client.party.id}] [{client_user_display_name}] {l("party_member_disconnect", f"{str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}]")}'))
            dstore(client_user_display_name,f'[{l("party")}/{client.party.id}] {l("party_member_disconnect", f"{str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}]")}')
    
    if client.party.me.leader is True:
        try:
            await member.kick()
        except Exception:
            if data['loglevel'] == "debug":
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

async def event_party_member_chatban(member: fortnitepy.PartyMember, reason: str) -> None:
    if member is None:
        return
    client=member.client
    if client.isready is False:
        return
    client_user_display_name=str(client.user.display_name)
    member_joined_at_most=[]
    for member_ in client.party.members.values():
        add_cache(client, member_)
        try:
            if member_joined_at_most != []:
                if member_.id in [i.user.id for i in loadedclients]:
                    if member_.id != client.user.id:
                        client_user_display_name+=f"/{str(member_.display_name)}"
                    if member_.joined_at < member_joined_at_most[1]:
                        member_joined_at_most=[member_.id, member_.joined_at]
            else:
                member_joined_at_most=[client.user.id, client.party.me.joined_at]
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    if member_joined_at_most == []:
        member_joined_at_most=[client.user.id]
    if client.user.id == member_joined_at_most[0]:
        if data['loglevel'] == 'normal':
            if reason is None:
                if data['no-logs'] is False:
                    print(magenta(f'[{now_()}] [{l("party")}] [{client_user_display_name}] {l("party_member_chatban", str(member.party.leader.display_name), str(member.display_name))}'))
                dstore(client_user_display_name,f'[{l("party")}] {l("party_member_chatban", str(member.party.leader.display_name), str(member.display_name))}')
            else:
                if data['no-logs'] is False:
                    print(magenta(f'[{now_()}] [{l("party")}] [{client_user_display_name}] {l("party_member_chatban2", str(member.party.leader.display_name), str(member.display_name), reason)}'))
                dstore(client_user_display_name,f'[{l("party")}] {l("party_member_chatban2", str(member.party.leader.display_name), str(member.display_name), reason)}')
        else:
            if reason is None:
                if data['no-logs'] is False:
                    print(magenta(f'[{now_()}] [{l("party")}/{client.party.id}] [{client_user_display_name}] {l("party_member_chatban", f"{str(member.party.leader.display_name)} / {member.party.leader.id} [{platform_to_str(member.party.leader.platform)}/{member.party.leader.input}]", f"{str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}]")}'))
                dstore(client_user_display_name,f'[{l("party")}/{client.party.id}] {l("party_member_chatban", f"{str(member.party.leader.display_name)} / {member.party.leader.id} [{platform_to_str(member.party.leader.platform)}/{member.party.leader.input}]", f"{str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}]")}')
            else:
                if data['no-logs'] is False:
                    print(magenta(f'[{now_()}] [{l("party")}/{client.party.id}] [{client_user_display_name}] {l("party_member_chatban2", f"{str(member.party.leader.display_name)} / {member.party.leader.id} [{platform_to_str(member.party.leader.platform)}/{member.party.leader.input}]", f"{str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}]", reason)}'))
                dstore(client_user_display_name,f'[{l("party")}/{client.party.id}] {l("party_member_chatban2", f"{str(member.party.leader.display_name)} / {member.party.leader.id} [{platform_to_str(member.party.leader.platform)}/{member.party.leader.input}]", f"{str(member.display_name)} / {member.id} [{platform_to_str(member.platform)}/{member.input}]", reason)}')

async def event_party_update(party: fortnitepy.Party) -> None:
    if party is None:
        return
    client=party.client
    if client.isready is False:
        return
    client_user_display_name=str(client.user.display_name)
    member_joined_at_most=[]
    for member_ in client.party.members.values():
        add_cache(client, member_)
        try:
            if member_joined_at_most != []:
                if member_.id in [i.user.id for i in loadedclients]:
                    if member_.id != client.user.id:
                        client_user_display_name+=f"/{str(member_.display_name)}"
                    if member_.joined_at < member_joined_at_most[1]:
                        member_joined_at_most=[member_.id, member_.joined_at]
            else:
                member_joined_at_most=[client.user.id, client.party.me.joined_at]
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    if member_joined_at_most == []:
        member_joined_at_most=[client.user.id]
    if client.user.id == member_joined_at_most[0]:
        if data['loglevel'] != 'normal':
            if data['no-logs'] is False:
                print(magenta(f'[{now_()}] [{l("party")}/{client.party.id}] [{client_user_display_name}] {l("party_update")}'))
            dstore(client_user_display_name,f'[{l("party")}/{client.party.id}] {l("party_update")}')

#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================

async def event_friend_message(message: fortnitepy.FriendMessage) -> None:
    global blacklist
    global whitelist
    global otherbotlist
    global blacklist_
    global whitelist_
    global kill
    if message is None:
        return
    client=message.client
    if data['discord']['enabled'] is True and dclient.isready is False:
        return
    if client.isready is False:
        return
    name=client.user.display_name
    author_id = message.author.id
    loop = asyncio.get_event_loop()
    add_cache(client, message.author)
    if message.author.id in blacklist and data['fortnite']['blacklist-ignorecommand'] is True:
        return
    if message.author.id in otherbotlist and data['fortnite']['ignorebot'] is True:
        return
    if client.owner is not None:
        if client.whisper is False:
            if client.whisperperfect is True:
                return
            elif message.author.id != client.owner.id and message.author.id not in whitelist:
                return
    else:
        if client.whisper is False:
            if message.author.id not in whitelist:
                return
    content=message.content
    if data['caseinsensitive'] is True:
        args = jaconv.kata2hira(content.lower()).split()
    else:
        args = content.split()
    rawargs = content.split()
    rawcontent = ' '.join(rawargs[1:])
    rawcontent2 = ' '.join(rawargs[2:])
    user=None
    if rawcontent in commands['me'].split(','):
        rawcontent=str(message.author.display_name)
    if data['loglevel'] == 'normal':
        if data['no-logs'] is False:
            print(f'[{now_()}] [{client.user.display_name}] {str(message.author.display_name)} | {content}')
        dstore(message.author.display_name,content)
    else:
        if data['no-logs'] is False:
            print(f'[{now_()}] [{client.user.display_name}] {str(message.author.display_name)}/ {message.author.id} [{platform_to_str(message.author.platform)}] | {content}')
        dstore(f'{message.author.display_name} / {message.author.id}',content)

    flag = False
    if isinstance(message, fortnitepy.message.MessageBase) is True:
        if client.owner is not None:
            if data['fortnite']['whitelist-ownercommand'] is True:
                if client.owner.id != message.author.id and message.author.id not in whitelist:
                    flag = True
            else:
                if client.owner.id != message.author.id:
                    flag = True
        else:
            if data['fortnite']['whitelist-ownercommand'] is True:
                if message.author.id not in whitelist:
                    flag = True
            else:
                flag = True
    else:
        if dclient.owner is not None:
            if data['discord']['whitelist-ownercommand'] is True:
                if client.owner.id != message.author.id and message.author.id not in whitelist_:
                    flag = True
            else:
                if client.owner.id != message.author.id:
                    flag = True
        else:
            if data['discord']['whitelist-ownercommand'] is True:
                if message.author.id not in whitelist_:
                    flag = True
            else:
                flag = True
    if flag is True:
        for checks in commands.items():
            if checks[0] in ignore:
                continue
            if commands['ownercommands'] == '':
                break
            for command in commands['ownercommands'].split(','):
                if args[0] in commands[command.lower()].split(','):
                    await reply(message, l("this_command_owneronly"))
                    return

    if args[0] in commands['prev'].split(','):
        if client.prevmessage.get(message.author.id) is None:
            client.prevmessage[message.author.id]='None'
        content=client.prevmessage.get(message.author.id)
        if data['caseinsensitive'] is True:
            args = jaconv.kata2hira(content.lower()).split()
        else:
            args = content.split()
        args = jaconv.kata2hira(content.lower()).split()
        rawargs = content.split()
        rawcontent = ' '.join(rawargs[1:])
        rawcontent2 = ' '.join(rawargs[2:])
    client.prevmessage[message.author.id]=content

    for key,value in replies.items():
        if args[0] in key.split(','):
            try:
                await reply(message, value)
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))
            return

    if data['discord']['enabled'] is True and dclient.isready is True:
        if args[0] in commands['addblacklist_discord'].split(','):
            try:
                if rawcontent == '' or args[1].isdigit() is False:
                    await reply(message, f"[{commands['addblacklist_discord']}] [{l('userid')}]")
                    return
                user = dclient.get_user(int(args[1]))
                if user is None:
                    user = await dclient.fetch_user(int(args[1]))
                if user.id not in blacklist_:
                    blacklist_.append(user.id)
                    data["discord"]["blacklist"].append(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["discord"]["blacklist"] = data["discord"]["blacklist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, l('add_to_list', f'{str(user)} / {str(user.id)}', l('discord_blacklist')))
                else:
                    await reply(message, l('already_list', f'{str(user)} / {user.id}', l('discord_blacklist')))
            except discord.NotFound:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('user_notfound'))
            except discord.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
                dstore(name,f'>>> {l("error_while_requesting_userinfo")}')
                await reply(message, l("error_while_requesting_userinfo"))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['removeblacklist_discord'].split(','):
            try:
                if rawcontent == '' or args[1].isdigit() is False:
                    await reply(message, f"[{commands['removeblacklist_discord']}] [{l('userid')}]")
                    return
                user = dclient.get_user(int(args[1]))
                if user is None:
                    user = await dclient.fetch_user(int(args[1]))
                if user.id in blacklist_:
                    blacklist_.remove(user.id)
                    data["discord"]["blacklist"].remove(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["discord"]["blacklist"] = data["discord"]["blacklist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, l('remove_from_list', f'{str(user)} / {user.id}', l('discord_blacklist')))
                else:
                    await reply(message, l('not_list', f'{str(user)} / {user.id}', l('discord_blacklist')))
            except discord.NotFound:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('user_notfound'))
            except discord.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
                dstore(name,f'>>> {l("error_while_requesting_userinfo")}')
                await reply(message, l("error_while_requesting_userinfo"))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['addwhitelist_discord'].split(','):
            try:
                if rawcontent == '' or args[1].isdigit() is False:
                    await reply(message, f"[{commands['addwhitelist_discord']}] [{l('userid')}]")
                    return
                user = dclient.get_user(int(args[1]))
                if user is None:
                    user = await dclient.fetch_user(int(args[1]))
                if user.id not in whitelist_:
                    whitelist_.append(user.id)
                    data["discord"]["whitelist"].append(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["discord"]["whitelist"] = data["discord"]["whitelist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, l('add_from_list', f'{str(user)} / {user.id}', l('discord_whitelist')))
                else:
                    await reply(message, l('already_list', f'{str(user)} / {user.id}', l('discord_whitelist')))
            except discord.NotFound:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('user_notfound'))
            except discord.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
                dstore(name,f'>>> {l("error_while_requesting_userinfo")}')
                await reply(message, l("error_while_requesting_userinfo"))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['removewhitelist_discord'].split(','):
            try:
                if rawcontent == '' or args[1].isdigit() is False:
                    await reply(message, f"[{commands['removewhitelist_discord']}] [{l('userid')}]")
                    return
                user = dclient.get_user(int(args[1]))
                if user is None:
                    user = await dclient.fetch_user(int(args[1]))
                if user.id in whitelist_:
                    whitelist_.remove(user.id)
                    data["discord"]["whitelist"].remove(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["discord"]["whitelist"] = data["discord"]["whitelist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, l('remove_list', f'{str(user)} / {user.id}', l('discord_whitelist')))
                else:
                    await reply(message, l('not_list', f'{str(user)} / {user.id}', l('discord_whitelist')))
            except discord.NotFound:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('user_notfound'))
            except discord.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
                dstore(name,f'>>> {l("error_while_requesting_userinfo")}')
                await reply(message, l("error_while_requesting_userinfo"))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

    if args[0] in commands['eval'].split(','):
        try:
            if rawcontent == "":
                await reply(message, f"[{commands['eval']}] [{l('eval')}]")
                return
            variable=globals()
            variable.update(locals())
            if rawcontent.startswith("await "):
                if data['loglevel'] == "debug":
                    print(f"await eval({rawcontent.replace('await ','',1)})")
                result = await eval(rawcontent.replace("await ","",1), variable)
                await reply(message, str(result))
            else:
                if data['loglevel'] == "debug":
                    print(f"eval {rawcontent}")
                result = eval(rawcontent, variable)
                await reply(message, str(result))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"{l('error')}\n{traceback.format_exc()}")

    elif args[0] in commands['exec'].split(','):
        try:
            if rawcontent == "":
                await reply(message, f"[{commands['exec']}] [{l('exec')}]")
                return
            variable=globals()
            variable.update(locals())
            args_=[i.replace("\\nn", "\n") for i in content.replace("\n", "\\nn").split()]
            content_=" ".join(args_[1:])
            result = await aexec(content_, variable)
            await reply(message, str(result))
        except Exception as e:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"{l('error')}\n{traceback.format_exc()}")

    elif args[0] in commands['restart'].split(','):
        try:
            flag = False
            if client.acceptinvite is False:
                if isinstance(message, fortnitepy.message.MessageBase) is True:
                    if client.owner is not None:
                        if data['fortnite']['whitelist-ownercommand'] is True:
                            if client.owner.id != message.author.id and message.author.id not in whitelist:
                                flag = True
                        else:
                            if client.owner.id != message.author.id:
                                flag = True
                    else:
                        if data['fortnite']['whitelist-ownercommand'] is True:
                            if message.author.id not in whitelist:
                                flag = True
                        else:
                            flag = True
                elif isinstance(message, discord.Message) is True:
                    if dclient.owner is not None:
                        if data['discord']['whitelist-ownercommand'] is True:
                            if dclient.owner.id != message.author.id and message.author.id not in whitelist_:
                                flag = True
                        else:
                            if dclient.owner.id != message.author.id:
                                flag = True
                    else:
                        if data['discord']['whitelist-ownercommand'] is True:
                            if message.author.id not in whitelist_:
                                flag = True
                        else:
                            flag = True
            if flag is True:
                await reply(message, l('invite_is_decline'))
                return
            await reply(message, l('restaring'))
            os.chdir(os.getcwd())
            os.execv(os.sys.executable,['python', *sys.argv])
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['relogin'].split(','):
        try:
            flag = False
            if client.acceptinvite is False:
                if isinstance(message, fortnitepy.message.MessageBase) is True:
                    if client.owner is not None:
                        if data['fortnite']['whitelist-ownercommand'] is True:
                            if client.owner.id != message.author.id and message.author.id not in whitelist:
                                flag = True
                        else:
                            if client.owner.id != message.author.id:
                                flag = True
                    else:
                        if data['fortnite']['whitelist-ownercommand'] is True:
                            if message.author.id not in whitelist:
                                flag = True
                        else:
                            flag = True
                elif isinstance(message, discord.Message) is True:
                    if dclient.owner is not None:
                        if data['discord']['whitelist-ownercommand'] is True:
                            if dclient.owner.id != message.author.id and message.author.id not in whitelist_:
                                flag = True
                        else:
                            if dclient.owner.id != message.author.id:
                                flag = True
                    else:
                        if data['discord']['whitelist-ownercommand'] is True:
                            if message.author.id not in whitelist_:
                                flag = True
                        else:
                            flag = True
            if flag is True:
                await reply(message, l('invite_is_decline'))
                return
            await reply(message, l('relogining'))
            await client.restart()
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['reload'].split(','):
        success=reload_configs(client)
        try:
            if success:
                await reply(message, l('success'))
            else:
                await reply(message, l('error'))
                return
            try:
                client.owner=None
                owner=await client.fetch_profile(data['fortnite']['owner'])
                if owner is None:
                    print(red(f'[{now_()}] [{client.user.display_name}] {l("owner_notfound")}'))
                    dstore(client.user.display_name,f'>>> {l("owner_notfound")}')
                else:
                    add_cache(client, owner)
                    client.owner=client.get_friend(owner.id)
                    if client.owner is None:
                        if data['fortnite']['addfriend'] is True:
                            try:
                                await client.add_friend(owner.id)
                            except fortnitepy.HTTPException:
                                if data['loglevel'] == 'debug':
                                    print(red(traceback.format_exc()))
                                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                                if data['loglevel'] == 'normal':
                                    print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_sending_friendrequest")}'))
                                    dstore(client.user.display_name,f'>>> {l("error_while_sending_friendrequest")}')
                                else:
                                    print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_sending_friendrequest")}'))
                                dstore(client.user.display_name,f'>>> {l("error_while_sending_friendrequest")}')
                            except Exception:
                                print(red(traceback.format_exc()))
                                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                        print(red(f'[{now_()}] [{client.user.display_name}] {l("not_friend_with_owner", commands["reload"])}'))
                        dstore(client.user.display_name,f'>>> {l("not_friend_with_owner", commands["reload"])}')
                    else:
                        if data['loglevel'] == 'normal':
                            if data['no-logs'] is False:
                                print(green(f'[{now_()}] [{client.user.display_name}] {l("owner")}: {str(client.owner.display_name)}'))
                            dstore(client.user.display_name,f'{l("owner")}: {str(client.owner.display_name)}')
                        else:
                            if data['no-logs'] is False:
                                print(green(f'[{now_()}] [{client.user.display_name}] {l("owner")}: {str(client.owner.display_name)} / {client.owner.id}'))
                            dstore(client.user.display_name,f'{l("owner")}: {str(client.owner.display_name)} / {client.owner.id}')
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
                dstore(client.user.display_name,f'>>> {l("error_while_requesting_userinfo")}')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

            for blacklistuser in data['fortnite']['blacklist']:
                try:
                    user = await client.fetch_profile(blacklistuser)
                    add_cache(client, user)
                    if user is None:
                        print(red(f'[{now_()}] [{client.user.display_name}] {l("blacklist_user_notfound", blacklistuser)}'))
                        dstore(client.user.display_name,f'>>> {l("blacklist_user_notfound", blacklistuser)}')
                    else:
                        blacklist.append(user.id)
                        if data['loglevel'] == 'debug':
                            print(yellow(f"{str(user.display_name)} / {user.id}"))
                        if data['fortnite']['blacklist-autoblock'] is True:
                            try:
                                await user.block()
                            except Exception:
                                if data['loglevel'] == 'debug':
                                    print(red(traceback.format_exc()))
                                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                    print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
                    dstore(client.user.display_name,f'>>> {l("error_while_requesting_userinfo")}')
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            if data['loglevel'] == "debug":
                print(yellow(blacklist))
            for whitelistuser in data['fortnite']['whitelist']:
                try:
                    user = await client.fetch_profile(whitelistuser)
                    add_cache(client, user)
                    if user is None:
                        print(red(f'[{now_()}] [{client.user.display_name}] {l("whitelist_user_notfound", whitelistuser)}'))
                        dstore(client.user.display_name,f'>>> {l("whitelist_user_notfound", whitelistuser)}')
                    else:
                        whitelist.append(user.id)
                        if data['loglevel'] == 'debug':
                            print(yellow(f"{str(user.display_name)} / {user.id}"))
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                    print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
                    dstore(client.user.display_name,f'>>> {l("error_while_requesting_userinfo")}')
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            if data['loglevel'] == "debug":
                print(yellow(whitelist))

            for invitelistuser in data['fortnite']['invitelist']:
                try:
                    user = await client.fetch_profile(invitelistuser)
                    if user is None:
                        print(red(f'[{now_()}] [{client.user.display_name}] {l("invitelist_user_notfound", invitelistuser)}'))
                        dstore(client.user.display_name,f'>>> {l("invitelist_user_notfound", invitelistuser)}')
                    else:
                        friend = client.get_friend(user.id)
                        if friend is None and user.id != client.user.id:
                            if data['fortnite']['addfriend'] is True:
                                try:
                                    await client.add_friend(friend.id)
                                except fortnitepy.HTTPException:
                                    if data['loglevel'] == 'debug':
                                        print(red(traceback.format_exc()))
                                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                                    if data['loglevel'] == 'normal':
                                        print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_sending_friendrequest")}'))
                                        dstore(client.user.display_name,f'>>> {l("error_while_sending_friendrequest")}')
                                    else:
                                        print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_sending_friendrequest")}'))
                                        dstore(client.user.display_name,f'>>> {l("error_while_sending_friendrequest")}')
                                except Exception:
                                    print(red(traceback.format_exc()))
                                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                            print(red(f'[{now_()}] [{client.user.display_name}] {l("not_friend_with_inviteuser", invitelistuser)}'))
                            dstore(client.user.display_name,f'>>> {l("not_friend_with_inviteuser", invitelistuser)}')
                        else:
                            add_cache(client, user)
                            client.invitelist.append(user.id)
                            if data['loglevel'] == 'debug':
                                print(yellow(f"{str(user.display_name)} / {user.id}"))
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                    print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
                    dstore(client.user.display_name,f'>>> {l("error_while_requesting_userinfo")}')
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            if data['loglevel'] == "debug":
                print(yellow(client.invitelist))
            if data['discord']['enabled'] is True:
                dclient_user = str(dclient.user)
                activity = discord.Game(name=data['discord']['status'])
                await dclient.change_presence(activity=activity)

                for blacklistuser in data['discord']['blacklist']:
                    user = dclient.get_user(blacklistuser)
                    if user is None:
                        try:
                            user = await dclient.fetch_user(blacklistuser)
                        except discord.NotFound:
                            if data['loglevel'] == "debug":
                                print(red(traceback.format_exc()))
                                dstore(dclient_user,f'>>> {traceback.format_exc()}')
                            user = None
                    if user is None:
                        print(red(f'[{now_()}] [{dclient_user}] {l("discord_blacklist_user_notfound", blacklistuser)}'))
                        dstore(dclient_user,f'>>> {l("discord_blacklist_user_notfound", blacklistuser)}')
                    else:
                        blacklist_.append(user.id)
                        if data['loglevel'] == 'debug':
                            print(yellow(f"{user} / {user.id}"))
                if data['loglevel'] == "debug":
                    print(yellow(blacklist_))
                for whitelistuser in data['discord']['whitelist']:
                    user = dclient.get_user(whitelistuser)
                    if user is None:
                        try:
                            user = await dclient.fetch_user(whitelistuser)
                        except discord.NotFound:
                            if data['loglevel'] == "debug":
                                print(red(traceback.format_exc()))
                                dstore(dclient_user,f'>>> {traceback.format_exc()}')
                            user = None
                    if user is None:
                        print(red(f'[{now_()}] [{dclient_user}] {l("discord_whitelist_user_notfound", whitelistuser)}'))
                        dstore(dclient_user,f'>>> {l("discord_whitelist_user_notfound", whitelistuser)}')
                    else:
                        whitelist_.append(user.id)
                        if data['loglevel'] == 'debug':
                            print(yellow(f"{user.display_name} / {user.id}"))
                if data['loglevel'] == "debug":
                    print(yellow(whitelist_))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['addblacklist'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['addblacklist']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(name) and user.id != client.user.id and user.id not in blacklist}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.id not in blacklist:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if user.id not in blacklist:
                    blacklist.append(user.id)
                    if user.display_name is not None:
                        data["fortnite"]["blacklist"].append(str(user.display_name))
                    else:
                        data["fortnite"]["blacklist"].append(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, l('add_to_list', f'{str(user.display_name)} / {user.id}', l('blacklist')))
                else:
                    await reply(message, l('already_in_list', f'{str(user.display_name)} / {user.id}', l('blacklist')))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
            if user.id not in blacklist:
                blacklist.append(user.id)
                if user.display_name is not None:
                    data["fortnite"]["blacklist"].append(str(user.display_name))
                else:
                    data["fortnite"]["blacklist"].append(user.id)
                try:
                    with open("config.json", "r", encoding="utf-8") as f:
                        data_ = json.load(f)
                except json.decoder.JSONDecodeError:
                    with open("config.json", "r", encoding="utf-8-sig") as f:
                        data_ = json.load(f)
                data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
                with open("config.json", "w", encoding="utf-8") as f:
                    json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                await reply(message, l('add_to_list', f'{str(user.display_name)} / {user.id}', l('blacklist')))
            else:
                await reply(message, l('already_in_list', f'{str(user.display_name)} / {user.id}', l('blacklist')))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_add_to_list', l('blacklist'))}"
                await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['removeblacklist'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['removeblacklist']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and user.id in blacklist}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.id in blacklist:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if user.id in blacklist:
                    blacklist.remove(user.id)
                    try:
                        data["fortnite"]["blacklist"].remove(str(user.display_name))
                    except ValueError:
                        data["fortnite"]["blacklist"].remove(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, l('remove_from_list', f'{str(user.display_name)} / {user.id}', l('blacklist')))
                else:
                    await reply(message, l('not_list', f'{str(user.display_name)} / {user.id}', l('blacklist')))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        if user.id in blacklist:
            blacklist.remove(user.id)
            try:
                data["fortnite"]["blacklist"].remove(str(user.display_name))
            except ValueError:
                data["fortnite"]["blacklist"].remove(user.id)
            try:
                with open("config.json", "r", encoding="utf-8") as f:
                    data_ = json.load(f)
            except json.decoder.JSONDecodeError:
                with open("config.json", "r", encoding="utf-8-sig") as f:
                    data_ = json.load(f)
            data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
            await reply(message, l('remove_from_list', f'{str(user.display_name)} / {user.id}', l('blacklist')))
        else:
            await reply(message, l('not_list', f'{str(user.display_name)} / {user.id}', l('blacklist')))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_remove_from_list', l('blacklist'))}"
                await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['addwhitelist'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['addwhitelist']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and user.id not in whitelist}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.id not in whitelist:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if user.id not in whitelist:
                    whitelist.append(user.id)
                    if user.display_name is not None:
                        data["fortnite"]["whitelist"].append(str(user.display_name))
                    else:
                        data["fortnite"]["whitelist"].append(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["fortnite"]["whitelist"] = data["fortnite"]["whitelist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, l("add_to_list", f"{str(user.display_name)} / {user.id}", l('whitelist')))
                else:
                    await reply(message, l("already_list", f"{str(user.display_name)} / {user.id}", l('whitelist')))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
            if user.id not in whitelist:
                whitelist.append(user.id)
                if user.display_name is not None:
                    data["fortnite"]["whitelist"].append(str(user.display_name))
                else:
                    data["fortnite"]["whitelist"].append(user.id)
                try:
                    with open("config.json", "r", encoding="utf-8") as f:
                        data_ = json.load(f)
                except json.decoder.JSONDecodeError:
                    with open("config.json", "r", encoding="utf-8-sig") as f:
                        data_ = json.load(f)
                data_["fortnite"]["whitelist"] = data["fortnite"]["whitelist"]
                with open("config.json", "w", encoding="utf-8") as f:
                    json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                await reply(message, l("add_to_list", f"{str(user.display_name)} / {user.id}", l('whitelist')))
            else:
                await reply(message, l("already_list", f"{str(user.display_name)} / {user.id}", l('whitelist')))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_add_to_list', l('whitelist'))}"
                await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['removewhitelist'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['removewhitelist']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and user.id in whitelist}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.id in whitelist:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l("too_many_users", str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if user.id in whitelist:
                    whitelist.remove(user.id)
                    try:
                        data["whitelist"].remove(str(user.display_name))
                    except ValueError:
                        data["whitelist"].remove(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["whitelist"] = data["whitelist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, l("remove_from_list", f"{str(user.display_name)} / {user.id}", l('whitelist')))
                else:
                    await reply(message, l("not_list", f"{str(user.display_name)} / {user.id}", l('whitelist')))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        if user.id in whitelist:
            whitelist.remove(user.id)
            try:
                data["whitelist"].remove(str(user.display_name))
            except ValueError:
                data["whitelist"].remove(user.id)
            try:
                with open("config.json", "r", encoding="utf-8") as f:
                    data_ = json.load(f)
            except json.decoder.JSONDecodeError:
                with open("config.json", "r", encoding="utf-8-sig") as f:
                    data_ = json.load(f)
            data_["whitelist"] = data["whitelist"]
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
            await reply(message, l("remove_from_list", f"{str(user.display_name)} / {user.id}", l('whitelist')))
        else:
            await reply(message, l("not_list", f"{str(user.display_name)} / {user.id}", l('whitelist')))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_remove_from_list', l('whitelist'))}"
                await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['addinvitelist'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['addinvitelist']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and user.id not in client.invitelist}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.id not in client.invitelist:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l("too_many_users", str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if user.id not in client.invitelist:
                    client.invitelist.append(user.id)
                    if user.display_name is not None:
                        data["fortnite"]["invitelist"].append(str(user.display_name))
                    else:
                        data["fortnite"]["invitelist"].append(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["fortnite"]["invitelist"] = data["fortnite"]["invitelist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, l("add_to_list", f"{str(user.display_name)} / {user.id}", l('invitelist')))
                else:
                    await reply(message, l("already_list", f"{str(user.display_name)} / {user.id}", l('invitelist')))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        if user.id not in client.invitelist:
            client.invitelist.append(user.id)
            if user.display_name is not None:
                data["fortnite"]["invitelist"].append(str(user.display_name))
            else:
                data["fortnite"]["invitelist"].append(user.id)
            try:
                with open("config.json", "r", encoding="utf-8") as f:
                    data_ = json.load(f)
            except json.decoder.JSONDecodeError:
                with open("config.json", "r", encoding="utf-8-sig") as f:
                    data_ = json.load(f)
            data_["fortnite"]["invitelist"] = data["fortnite"]["invitelist"]
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
            await reply(message, l("add_to_list", f"{str(user.display_name)} / {user.id}", l('invitelist')))
        else:
            await reply(message, l("already_list", f"{str(user.display_name)} / {user.id}", l('invitelist')))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_add_to_list', l('invitelist'))}"
                await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['removeinvitelist'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['removeinvitelist']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and user.id in client.invitelist}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.id in client.invitelist:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l("too_many_users", str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if user.id in client.invitelist:
                    client.invitelist.remove(user.id)
                    try:
                        data["fortnite"]["invitelist"].remove(str(user.display_name))
                    except ValueError:
                        data["fortnite"]["invitelist"].remove(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["fortnite"]["invitelist"] = data["fortnite"]["invitelist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, l("remove_from_list", f"{str(user.display_name)} / {user.id}", l('invitelist')))
                else:
                    await reply(message, l("not_list", f"{str(user.display_name)} / {user.id}", l('invitelist')))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        if user.id in client.invitelist:
            client.invitelist.remove(user.id)
            try:
                data["fortnite"]["invitelist"].remove(str(user.display_name))
            except ValueError:
                data["fortnite"]["invitelist"].remove(user.id)
            try:
                with open("config.json", "r", encoding="utf-8") as f:
                    data_ = json.load(f)
            except json.decoder.JSONDecodeError:
                with open("config.json", "r", encoding="utf-8-sig") as f:
                    data_ = json.load(f)
            data_["fortnite"]["invitelist"] = data["fortnite"]["invitelist"]
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
            await reply(message, l("remove_from_list", f"{str(user.display_name)} / {user.id}", l('invitelist')))
        else:
            await reply(message, l("not_list", f"{str(user.display_name)} / {user.id}", l('invitelist')))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_remove_from_list', l('invitelist'))}"
                await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['get'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['get']}] [{l('name_or_id')}]")
                return
            users = {str(member.display_name): member for member in client.party.members.values() if rawcontent in str(member.display_name)}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.party.members.get(user.id) is not None:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l("too_many_users", str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                member=client.party.members.get(user.id)
                if member is None:
                    await reply(message, l("user_not_in_party"))
                    return
                if data['no-logs'] is False:
                    print(f'{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}')
                if data['loglevel'] == 'debug':
                    print(json.dumps(member.meta.schema, indent=2))
                dstore(name,f'{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}')
                await reply(message, f'{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}')
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        member=client.party.members.get(user.id)
        if member is None:
            await reply(message, l("user_not_in_party"))
            return
        if data['no-logs'] is False:
            print(f'''{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}''')
        if data['loglevel'] == 'debug':
            print(json.dumps(member.meta.schema, indent=2))
        dstore(name,f'''{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}''')
        await reply(message, f'''{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}''')""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_get_userinfo')}"
                await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['friendcount'].split(','):
        try:
            if data['no-logs'] is False:
                print(f"{l('friendcount')}: {len(client.friends)}")
            dstore(name,f"{l('friendcount')}: {len(client.friends)}")
            await reply(message, f"{l('friendcount')}: {len(client.friends)}")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['pendingcount'].split(','):
        try:
            outbound = []
            inbound = []
            for pending in client.pending_friends.values():
                if pending.direction == 'OUTBOUND':
                    outbound.append(pending)
                elif pending.direction == 'INBOUND':
                    inbound.append(pending)
            if data['no-logs'] is False:
                print(f"{l('pendingcount')}: {len(client.pending_friends)}\n{l('outbound')}: {len(outbound)}\n{l('inbound')}: {len(inbound)}")
            dstore(name,f"{l('pendingcount')}: {len(client.pending_friends)}\n{l('outbound')}: {len(outbound)}\n{l('inbound')}: {len(inbound)}")
            await reply(message, f"{l('pendingcount')}: {len(client.pending_friends)}\n{l('outbound')}: {len(outbound)}\n{l('inbound')}: {len(inbound)}")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['blockcount'].split(','):
        try:
            if data['no-logs'] is False:
                print(f"{l('blockcount')}: {len(client.blocked_users)}")
            dstore(name,f"{l('blockcount')}: {len(client.blocked_users)}")
            await reply(message, f"{l('blockcount')}: {len(client.blocked_users)}")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['friendlist'].split(','):
        try:
            text=''
            for friend in client.friends.values():
                add_cache(client, friend)
                text+=f'\n{str(friend.display_name)}'
            if data['no-logs'] is False:
                print(f'{text}')
            dstore(name,f'{text}')
            await reply(message, f'{text}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['pendinglist'].split(','):
        try:
            outbound=''
            inbound=''
            for pending in client.pending_friends.values():
                add_cache(client, pending)
                if pending.direction == 'OUTBOUND':
                    outbound+=f'\n{str(pending.display_name)}'
                elif pending.direction == 'INBOUND':
                    inbound+=f'\n{str(pending.display_name)}'
            if data['no-logs'] is False:
                print(f"{l('outbound')}: {outbound}\n{l('inbound')}: {inbound}")
            dstore(name,f"{l('outbound')}: {outbound}\n{l('inbound')}: {inbound}")
            await reply(message, f"{l('outbound')}: {outbound}\n{l('inbound')}: {inbound}")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['blocklist'].split(','):
        try:
            text=''
            for block in client.blocked_users.values():
                add_cache(client, block)
                text+=f'\n{str(block.display_name)}'
            if data['no-logs'] is False:
                print(f'{text}')
            dstore(name,f'{text}')
            await reply(message, f'{text}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['outfitmimic'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.outfitmimic=True
                await reply(message, l('set_to', l('mimic', l('outfit')), l('on')))
            elif args[1] in commands['false'].split(','):
                client.outfitmimic=False
                await reply(message, l('set_to', l('mimic', l('outfit')), l('off')))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['skinmimic']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['backpackmimic'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.backpackmimic=True
                await reply(message, l('mimic_set', l('set_to', l('mimic', l('backpack')), l('on'))))
            elif args[1] in commands['false'].split(','):
                client.backpackmimic=False
                await reply(message, l('mimic_set', l('set_to', l('mimic', l('backpack')), l('off'))))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['skinmimic']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['pickaxemimic'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.pickaxemimic=True
                await reply(message, l('mimic_set', l('set_to', l('mimic', l('pickaxe')), l('on'))))
            elif args[1] in commands['false'].split(','):
                client.pickaxemimic=False
                await reply(message, l('mimic_set', l('set_to', l('mimic', l('pickaxe')), l('off'))))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['skinmimic']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['emotemimic'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.emotemimic=True
                await reply(message, l('mimic_set', l('set_to', l('mimic', l('emote')), l('on'))))
            elif args[1] in commands['false'].split(','):
                client.emotemimic=False
                await reply(message, l('mimic_set', l('set_to', l('mimic', l('emote')), l('off'))))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['emotemimic']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['whisper'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.whisper=True
                await reply(message, l('set_to', l('command_from', l('whisper'), l('on'))))
            elif args[1] in commands['false'].split(','):
                client.whisper=False
                await reply(message, l('set_to', l('command_from', l('whisper'), l('off'))))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['whisper']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['partychat'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.partychat=True
                await reply(message, l('set_to', l('command_from', l('partychat'), l('on'))))
            elif args[1] in commands['false'].split(','):
                client.partychat=False
                await reply(message, l('set_to', l('command_from', l('partychat'), l('off'))))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['party']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['discord'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.discord=True
                await reply(message, l('set_to', l('command_from', l('discord'), l('on'))))
            elif args[1] in commands['false'].split(','):
                client.discord=False
                await reply(message, l('set_to', l('command_from', l('discord'), l('off'))))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['discord']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['disablewhisperperfectly'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.whisperperfect=True
                await reply(message, l('set_to', l('disable_perfect', l('whisper'), l('on'))))
            elif args[1] in commands['false'].split(','):
                client.whisperperfect=False
                await reply(message, l('set_to', l('disable_perfect', l('whisper'), l('off'))))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['disablewhisperperfectly']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['disablepartychatperfectly'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.partychatperfect=True
                await reply(message, l('set_to', l('disable_perfect', l('partychat'), l('on'))))
            elif args[1] in commands['false'].split(','):
                client.partychatperfect=False
                await reply(message, l('set_to', l('disable_perfect', l('partychat'), l('on'))))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['disablepartychatperfectly']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['disablediscordperfectly'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.discordperfect=True
                await reply(message, l('set_to', l('disable_perfect', l('discord'), l('on'))))
            elif args[1] in commands['false'].split(','):
                client.discordperfect=False
                await reply(message, l('set_to', l('disable_perfect', l('discord'), l('on'))))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['disablediscordperfectly']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['acceptinvite'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.acceptinvite=True
                await reply(message, l('set_to', l('invite'), l('accept')))
            elif args[1] in commands['false'].split(','):
                client.acceptinvite=False
                await reply(message, l('set_to', l('invite'), l('decline')))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['acceptinvite']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['acceptfriend'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.acceptfriend=True
                await reply(message, l('set_to', l('friendrequest'), l('accept')))
            elif args[1] in commands['false'].split(','):
                client.acceptfriend=False
                await reply(message, l('set_to', l('friendrequest'), l('decline')))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['acceptfriend']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['joinmessageenable'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.joinmessageenable=True
                await reply(message, l('set_to', l('join_', l('message')), l('on')))
            elif args[1] in commands['false'].split(','):
                client.joinmessageenable=False
                await reply(message, l('set_to', l('join_', l('message')), l('off')))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['joinmessageenable']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['randommessageenable'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.randommessageenable=True
                await reply(message, l('set_to', l('join_', l('randommessage')), l('on')))
            elif args[1] in commands['false'].split(','):
                client.randommessageenable=False
                await reply(message, l('set_to', l('join_', l('randommessage')), l('off')))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['randommessageenable']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['wait'].split(','):
        try:
            if client.owner is None:
                client.acceptinvite=False
                try:
                    client.timer_.cancel()
                except AttributeError:
                    pass
                client.timer_=Timer(data['fortnite']['waitinterval'], inviteaccept, [client])
                client.timer_.start()
                await reply(message, l('decline_invite_for', str(data['fortnite']['waitinterval'])))
            else:
                if client.owner.id in client.party.members.keys() and message.author.id != client.owner.id:
                    await reply(message, l('not_available'))
                    return
                client.acceptinvite=False
                try:
                    client.timer_.cancel()
                except AttributeError:
                    pass
                client.timer_=Timer(data['fortnite']['waitinterval'], inviteaccept, [client])
                client.timer_.start()
                await reply(message, l('decline_invite_for', str(data['fortnite']['waitinterval'])))
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['join'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['join']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.has_friend(user.id) is True:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                friend=client.get_friend(user.id)
                if friend is None:
                    await reply(message, l('not_friend_with_user'))
                else:
                    await friend.join_party()
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            friend=client.get_friend(user.id)
            if friend is None:
                await reply(message, l('not_friend_with_user'))
            else:
                await friend.join_party()
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('party_full_or_already_or_offline'))
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('party_notfound'))
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('party_private'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_joining_to_party'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"{l('enter_join_party')}"
                await reply(message, text)
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('party_full_or_already_or_offline'))
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('party_notfound'))
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('party_private'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_joining_to_party'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['joinid'].split(','):
        try:
            await client.join_to_party(party_id=args[1])
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('party_full_or_already'))
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('party_notfound'))
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('party_private'))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['join']}] [{l('party_id')}]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['leave'].split(','):
        try:
            await client.party.me.leave()
            await reply(message, l('party_leave', client.user.party.id))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_leaving_party'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['invite'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['invite']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.has_friend(user.id) is True:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                friend=client.get_friend(user.id)
                if friend is None:
                    await reply(message, l('not_friend_with_user'))
                    return
                await friend.invite()
                await reply(message, l('user_invited', f'{str(friend.display_name)} / {friend.id}', client.party.id))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            friend=client.get_friend(user.id)
            if friend is None:
                await reply(message, l('not_friend_with_user'))
                return
            await friend.invite()
            await reply(message, l('user_invited', f'{str(friend.display_name)} / {friend.id}', client.party.id))
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('party_full_or_already'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_sending_partyinvite'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_invite_user')}"
                await reply(message, text)
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('party_full_or_already'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_sending_partyinvite'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['inviteall'].split(','):
        try:
            for inviteuser in client.invitelist:
                if inviteuser != client.user.id and inviteuser not in client.party.members:
                    try:
                        await client.party.invite(inviteuser)
                    except fortnitepy.PartyError:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(name,f'>>> {traceback.format_exc()}')
                        await reply(message, l('party_full_or_already'))
                    except fortnitepy.Forbidden:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(name,f'>>> {traceback.format_exc()}')
                        await reply(message, l('not_friend_with_user'))
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(name,f'>>> {traceback.format_exc()}')
                        await reply(message, l('error_while_sending_partyinvite'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['message'].split(','):
        try:
            send=rawcontent.split(' : ')
            users = {str(user.display_name): user for user in cache_users.values() if send[0] in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is True}
            try:
                user=await client.fetch_profile(send[0])
                if user is not None:
                    if client.has_friend(user.id) is True:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                friend=client.get_friend(user.id)
                if friend is None:
                    await reply(message, l('not_friend_with_user'))
                    return
                await friend.send(send[1])
                await reply(message, l('user_sent', f'{str(friend.display_name)} / {friend.id}', send[1]))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            friend=client.get_friend(user.id)
            if friend is None:
                await reply(message, l('not_friend_with_user'))
                return
            await friend.send(send[1])
            await reply(message, l('user_sent', f'{str(friend.display_name)} / {friend.id}', send[1]))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l("error_while_requesting_userinfo"))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user, "send": send} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_send')}"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l("error_while_requesting_userinfo"))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['message']}] [{l('name_or_id')}] : [{l('content')}]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['partymessage'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['partymessage']}] [{l('content')}]")
                return
            await client.party.send(rawcontent)
            await reply(message, l('party_sent', client.party.id, rawcontent))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['status'].split(','):
        try:
            await client.set_status(rawcontent)
            await reply(message, l('set_to', l('status'), rawcontent))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['status']}] [{l('content')}]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['banner'].split(','):
        try:
            await client.party.me.edit_and_keep(partial(client.party.me.set_banner,args[1],args[2],client.party.me.banner[2]))
            await reply(message, l('set_to', l('banner'), f"{args[1]}, {args[2]}"))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_changing_asset'))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['banner']}] [{l('bannerid')}] [{l('color')}]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['level'].split(','):
        try:
            await client.party.me.edit_and_keep(partial(client.party.me.set_banner,client.party.me.banner[0],client.party.me.banner[1],int(args[1])))
            await reply(message, l('level', args[1]))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_changing_asset'))
        except ValueError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('must_be_int'))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['level']}] [{l('level')}]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['bp'].split(','):
        try:
            await client.party.me.edit_and_keep(partial(client.party.me.set_battlepass_info,True,args[1],args[2],args[3]))
            await reply(message, l('set_to', l('bpinfo'), f"{l('tier')}: {args[1]}, {l('xpboost')}: {args[2]}, {l('friendxpboost')}: {args[3]}"))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_changing_bpinfo'))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['bp']}] [{l('tier')}] [{l('xpboost')}] [{l('friendxpboost')}]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['privacy'].split(','):
        try:
            if args[1] in commands['privacy_public'].split(','):
                await client.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)
                await reply(message, l('set_to', l('privacy'), l('public')))
            elif args[1] in commands['privacy_friends_allow_friends_of_friends'].split(','):
                await client.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS_ALLOW_FRIENDS_OF_FRIENDS)
                await reply(message, l('set_to', l('privacy'), l('friends_allow_friends_of_friends')))
            elif args[1] in commands['privacy_friends'].split(','):
                await client.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS)
                await reply(message, l('set_to', l('privacy'), l('friends')))
            elif args[1] in commands['privacy_private_allow_friends_of_friends'].split(','):
                await client.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE_ALLOW_FRIENDS_OF_FRIENDS)
                await reply(message, l('set_to', l('privacy'), l('private_allow_friends_of_friends')))
            elif args[1] in commands['privacy_private'].split(','):
                await client.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE)
                await reply(message, l('set_to', l('privacy'), l('private')))
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('not_party_leader'))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['privacy']}] [[{commands['privacy_public']}] / [{commands['privacy_friends_allow_friends_of_friends']}] / [{commands['privacy_friends']}] / [{commands['privacy_private_allow_friends_of_friends']}] / [{commands['privacy_private']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error')) 

    elif args[0] in commands['getuser'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['getuser']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    users[str(user.display_name)] = user
                    add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            text = str()
            for user in users.values():
                text += f'\n{str(user.display_name)} / {user.id}'
            if data['no-logs'] is False:
                print(text)
            dstore(name,text)
            await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['getfriend'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['getfriend']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.has_friend(user.id) is True:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            text = str()
            for user in users.values():
                friend=client.get_friend(user.id)
                if friend is None:
                    continue
                if friend.nickname is None:
                    text += f'\n{str(friend.display_name)} / {friend.id}'
                else:
                    text += f'\n{friend.nickname}({str(friend.display_name)}) / {friend.id}'
                if friend.last_logout is not None:
                    text += "\n{1}: {0.year}/{0.month}/{0.day} {0.hour}:{0.minute}:{0.second}".format(friend.last_logout, l('lastlogin'))
            if data['no-logs'] is False:
                print(text)
            dstore(name,text)
            await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['getpending'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['getpending']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.is_pending(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.is_pending(user.id) is True:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            text = str()
            for user in users.values():
                pending = client.get_pending_friend(user.id)
                if pending is None:
                    continue
                text += f'\n{str(pending.display_name)} / {pending.id}'
            if data['no-logs'] is False:
                print(text)
            dstore(name,text)
            await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['getblock'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['getblock']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.is_blocked(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.is_blocked(user.id) is True:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            text = str()
            for user in users.values():
                block=client.get_blocked_user(user.id)
                if block is None:
                    continue
                text += f'\n{str(block.display_name)} / {block.id}'
            if data['no-logs'] is False:
                print(text)
            dstore(name,text)
            await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['info'].split(','):
        try:
            if args[1] in commands['info_party'].split(','):
                text = str()
                text += f"{client.party.id}\n{l('member_count')}: {client.party.member_count}"
                for member in client.party.members.values():
                    add_cache(client, member)
                    if data['loglevel'] == 'normal':
                        text += f'\n{str(member.display_name)}'
                    else:
                        text += f'\n{str(member.display_name)} / {member.id}'
                print(text)
                dstore(None, text)
                await reply(message, text)
                if data['loglevel'] == 'debug':
                    print(json.dumps(client.party.meta.schema, indent=2))
            
            elif True in [args[1] in commands[key].split(',') for key in ("cid", "bid", "petcarrier", "pickaxe_id", "eid", "emoji_id", "toy_id", "id")]:
                type_ = convert_to_type(args[1])
                if rawcontent2 == '':
                    await reply(message, f"[{commands[type_]}] [ID]")
                    return
                result = await loop.run_in_executor(None, search_item, data["lang"], "id", rawcontent2, type_)
                if result is None:
                    result = await loop.run_in_executor(None, search_item, "en", "id", rawcontent2, type_)
                if result is None:
                    await reply(message, l('item_notfound'))
                else:
                    if len(result) > 30:
                        await reply(message, l('too_many_items', str(len(result))))
                        return
                    if len(result) == 1:
                        await reply(message, f"{result[0]['type']['displayValue']}: {result[0]['name']} | {result[0]['id']}\n{result[0]['description']}\{result[0]['rarity']['displayValue']}\n{result[0]['set']['value']}")
                    else:
                        text = str()
                        for count, item in enumerate(result):
                            text += f"\n{count+1} {item['type']['displayValue']}: {item['name']} | {item['id']}"
                        text += f"\n{l('enter_to_show_info')}"
                        await reply(message, text)
                        client.select[message.author.id] = {"exec": [f"await reply(message, f'''{item['type']['displayValue']}: {item['name']} | {item['id']}\n{item['description']}\n{item['rarity']['displayValue']}\n{item['set']['value']}''')" for item in result]}

            elif True in  [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe", "emote", "emoji", "toy", "item")]:
                type_ = convert_to_type(args[1])
                if rawcontent2 == '':
                    await reply(message, f"[{commands[type_]}] [{l('itemname')}]")
                    return
                result = await loop.run_in_executor(None, search_item, data["lang"], "name", rawcontent2, type_)
                if result is None:
                    result = await loop.run_in_executor(None, search_item, "en", "name", rawcontent2, type_)
                if result is None:
                    await reply(message, l('item_notfound'))
                else:
                    if len(result) > 30:
                        await reply(message, l('too_many_items', str(len(result))))
                        return
                    if len(result) == 1:
                        await reply(message, f"{result[0]['type']['displayValue']}: {result[0]['name']} | {result[0]['id']}\n{result[0]['description']}\n{result[0]['rarity']['displayValue']}\n{result[0]['set']['value']}")
                    else:
                        text = str()
                        for count, item in enumerate(result):
                            text += f"\n{count+1} {item['type']['displayValue']}: {item['name']} | {item['id']}"
                        text += f"\n{l('enter_to_show_info')}"
                        await reply(message, text)
                        client.select[message.author.id] = {"exec": [f"await reply(message, f'''{item['type']['displayValue']}: {item['name']} | {item['id']}\n{item['description']}\n{item['rarity']['displayValue']}\n{item['set']['value']}''')" for item in result]}
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['info']}] [[{commands['info_party']}] / [{commands['info_item']}] / [{commands['id']}] / [{commands['skin']}] / [{commands['bag']}] / [{commands['pickaxe']}] / [{commands['emote']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['pending'].split(','):
        try:
            pendings=[]
            for pending in client.pending_friends.values():
                add_cache(client, pending)
                if pending.direction == 'INBOUND':
                    pendings.append(pending)
            if args[1] in commands['true'].split(','):
                for pending in pendings:
                    try:
                        await pending.accept()
                        await reply(message, l('add_friend', f'{str(pending.display_name)} / {pending.id}'))
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                        await reply(message, l('error_while_sending_friendrequest'))
                        continue
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                        await reply(message, l('error'))
                        continue
            elif args[1] in commands['false'].split(','):
                for pending in pendings:
                    try:
                        await pending.decline()
                        await reply(message, l('friend_request_decline', f'{str(pending.display_name)} / {pending.id}'))
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(name,f'>>> {traceback.format_exc()}')
                        await reply(message, l('error_while_declining_friendrequest'))
                        continue
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                        await reply(message, l('error'))
                        continue
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['pending']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['removepending'].split(','):
        try:
            pendings=[]
            for pending in client.pending_friends.values():
                add_cache(client, pending)
                if pending.direction == 'OUTBOUND':
                    pendings.append(pending)
            for pending in pendings:
                try:
                    await pending.decline()
                    await reply(message, l('remove_pending', f'{str(pending.display_name)} / {pending.id}'))
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l('error_while_removing_friendrequest'))
                    continue
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l('error'))
                    continue
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['addfriend'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['addfriend']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is False}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.has_friend(user.id) is False:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.has_friend(user.id) is True:
                    await reply(message, l('already_friend'))
                    return
                await client.add_friend(user.id)
                await reply(message, l('friend_request_to', f'{str(user.display_name)} / {user.id}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.has_friend(user.id) is True:
                await reply(message, l('already_friend'))
                return
            await client.add_friend(user.id)
            await reply(message, l('friend_request_to', f'{str(user.display_name)} / {user.id}'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_sending_friendrequest'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_send_friendrequest')}"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_sending_friendrequest'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['removefriend'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['removefriend']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.has_friend(user.id) is True:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.has_friend(user.id) is False:
                    await reply(message, l('not_friend_with_user'))
                    return
                await client.remove_or_decline_friend(user.id)
                await reply(message, l('remove_friend', f'{str(user.display_name)} / {user.id}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.has_friend(user.id) is False:
                await reply(message, l('not_friend_with_user'))
                return
            await client.remove_or_decline_friend(user.id)
            await reply(message, l('remove_friend', f'{str(user.display_name)} / {user.id}'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_removing_friend')""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_remove_friend')}"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_removing_friend'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['acceptpending'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['acceptpending']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.is_pending(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.is_pending(user.id) is True:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.is_pending(user.id) is False:
                    await reply(message, l('not_pending_with_user'))
                    return
                await client.accept_friend(user.id)
                await reply(message, l('friend_add', f'{str(user.display_name)} / {user.id}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.is_pending(user.id) is False:
                await reply(message, l('not_pending_with_user'))
                return
            await client.accept_friend(user.id)
            await reply(message, l('friend_add', f'{str(user.display_name)} / {user.id}'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_accepting_friendrequest'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_accept_pending')}"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_accepting_friendrequest'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['declinepending'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['declinepending']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.is_pending(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.is_pending(user.id) is True:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.is_pending(user.id) is False:
                    await reply(message, l('nor_pending_with_user'))
                    return
                await client.remove_or_decline_friend(user.id)
                await reply(message, l('friend_request_decline', f'{str(user.display_name)} / {user.id}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.is_pending(user.id) is False:
                await reply(message, l('nor_pending_with_user'))
                return
            await client.remove_or_decline_friend(user.id)
            await reply(message, l('friend_request_decline', f'{str(user.display_name)} / {user.id}'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_declining_friendrequest'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_decline_pending')}"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_declining_friendrequest'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['blockfriend'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['blockfriend']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.is_blocked(user.id) is False}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.is_blocked(user.id) is False:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.is_blocked(user.id) is True:
                    await reply(message, l('already_block'))
                    return
                await client.block_user(user.id)
                await reply(message, l('block_user', f'{str(user.display_name)} / {user.id}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.is_blocked(user.id) is True:
                await reply(message, l('already_block'))
                return
            await client.block_user(user.id)
            await reply(message, l('block_user', f'{str(user.display_name)} / {user.id}'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_blocking_user'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_block_user')}"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_blocking_user'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['unblockfriend'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['unblockfriend']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.is_blocked(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.is_blocked(user.id) is True:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.is_blocked(user.id) is False:
                    await reply(message, l('not_block'))
                    return
                await client.unblock_user(user.id)
                await reply(message, l('unblock_user', f'{str(user.display_name)} / {user.id}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.is_blocked(user.id) is False:
                await reply(message, l('not_block'))
                return
            await client.unblock_user(user.id)
            await reply(message, l('unblock_user', f'{str(user.display_name)} / {user.id}'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_unblocking_user'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_unblock_user')}"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_unblocking_user'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['chatban'].split(','):
        try:
            reason=rawcontent.split(' : ')
            if rawcontent == '':
                await reply(message, f"[{commands['chatban']}] [{l('name_or_id')}] : [{l('reason')}({l('optional')})]")
                return
            users = {str(member.display_name): member for member in client.party.members.values() if rawcontent in str(member.display_name)}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.party.members.get(user.id) is not None:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.party.members.get(user.id) is None:
                    await reply(message, l('user_not_in_party'))
                    return
                member=client.party.members.get(user.id)
                try:
                    await member.chatban(reason[1])
                except IndexError:
                    await member.chatban()
                await reply(message, l('chatban_user', f'{str(user.display_name)} / {user.id}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.party.members.get(user.id) is None:
                await reply(message, l('user_not_in_party'))
                return
            member=client.party.members.get(user.id)
            try:
                await member.chatban(reason[1])
            except IndexError:
                await member.chatban()
            await reply(message, l('chatban_user', f'{str(user.display_name)} / {user.id}'))
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('nor_party_leader'))
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('user_notfound'))
        except ValueError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('already_chatban'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user, "reason": reason} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_chatban')}"
                await reply(message, text)
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('nor_party_leader'))
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('user_notfound'))
        except ValueError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('already_chatban'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['promote'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['promote']}] [{l('name_or_id')}]")
                return
            users = {str(member.display_name): member for member in client.party.members.values() if rawcontent in str(member.display_name)}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.party.members.get(user.id) is not None:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.party.members.get(user.id) is None:
                    await reply(message, l('user_not_in_party'))
                    return
                member=client.party.members.get(user.id)
                await member.promote()
                await reply(message, l('promote_user', f'{str(user.display_name)} / {user.id}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.party.members.get(user.id) is None:
                await reply(message, l('user_not_in_party'))
                return
            member=client.party.members.get(user.id)
            await member.promote()
            await reply(message, l('promote_user', f'{str(user.display_name)} / {user.id}'))
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('not_party_leader'))
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('already_party_leader'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_promoting_party_leader'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_promote_user')}"
                await reply(message, text)
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('not_party_leader'))
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('already_party_leader'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_promoting_party_leader'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['kick'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['kick']}] [{l('name_or_id')}]")
                return
            users = {str(member.display_name): member for member in client.party.members.values() if rawcontent in str(member.display_name)}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.party.members.get(user.id) is not None:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.party.members.get(user.id) is None:
                    await reply(message, l('user_not_in_party'))
                    return
                member=client.party.members.get(user.id)
                await member.kick()
                await reply(message, l('kick_user', f'{str(user.display_name)} / {user.id}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.party.members.get(user.id) is None:
                await reply(message, l('user_not_in_party'))
                return
            member=client.party.members.get(user.id)
            await member.kick()
            await reply(message, l('kick_user', f'{str(user.display_name)} / {user.id}'))
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('not_party_leader'))
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('cant_kick_yourself'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_kicking_user'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += "\n数字を入力することでそのユーザーをキックします"
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('not_party_leader'))
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('cant_kick_yourself'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_kicking_user'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['ready'].split(','):
        try:
            await client.party.me.set_ready(fortnitepy.ReadyState.READY)
            await reply(message, l('set_to', l('readystate'), l('ready')))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['unready'].split(','):
        try:
            await client.party.me.set_ready(fortnitepy.ReadyState.NOT_READY)
            await reply(message, l('set_to', l('readystate'), l('unready')))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['sitout'].split(','):
        try:
            await client.party.me.set_ready(fortnitepy.ReadyState.SITTING_OUT)
            await reply(message, l('set_to', l('readystate'), l('sitout')))
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['match'].split(','):
        try:
            await client.party.me.set_in_match(players_left=int(args[1]) if args[1:2] else 100)
            await reply(message, l('set_to', l('matchstate'), l('remaining', args[1] if args[1:2] else "100")))
        except ValueError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('remaining_must_be_between_0_and_255'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['unmatch'].split(','):
        try:
            await client.party.me.clear_in_match()
            await reply(message, l('set_to', l('matchstate'), l('off')))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['swap'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['kick']}] [{l('name_or_id')}]")
                return
            users = {str(member.display_name): member for member in client.party.members.values() if rawcontent in str(member.display_name)}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.party.members.get(user.id) is not None:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.party.members.get(user.id) is None:
                    await reply(message, l('user_not_in_party'))
                    return
                member=client.party.members.get(user.id)
                await member.swap_position()
                await reply(message, l('swap_user', f'{str(user.display_name)} / {user.id}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.party.members.get(user.id) is None:
                await reply(message, l('user_not_in_party'))
                return
            member=client.party.members.get(user.id)
            await member.swap_position()
            await reply(message, l('swap_user', f'{str(user.display_name)} / {user.id}'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_swapping_user'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_swap_user')}"
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_swapping_user'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['outfitlock'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.outfitlock=True
                await reply(message, l('set_to', l('lock', l('outfit')), l('on')))
            elif args[1] in commands['false'].split(','):
                client.outfitlock=False
                await reply(message, l('set_to', l('lock', l('outfit')), l('off')))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['outfitlock']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['backpacklock'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.backpacklock=True
                await reply(message, l('set_to', l('lock', l('backpack')), l('on')))
            elif args[1] in commands['false'].split(','):
                client.backpacklock=False
                await reply(message, l('set_to', l('lock', l('backpack')), l('off')))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['backpacklock']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['pickaxelock'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.pickaxelock=True
                await reply(message, l('set_to', l('lock', l('pickaxe')), l('on')))
            elif args[1] in commands['false'].split(','):
                client.pickaxelock=False
                await reply(message, l('set_to', l('lock', l('pickaxe')), l('off')))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['pickaxelock']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['emotelock'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.emotelock=True
                await reply(message, l('set_to', l('lock', l('emote')), l('on')))
            elif args[1] in commands['false'].split(','):
                client.emotelock=False
                await reply(message, l('set_to', l('lock', l('emote')), l('off')))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['outfitlock']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['stop'].split(','):
        try:
            client.stopcheck=True
            if await change_asset(client, message.author.id, "emote", "") is True:
                await reply(message, l('stopped'))
            else:
                await reply(message, l('locked'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['alloutfit'].split(','):
        try:
            flag = False
            if client.outfitlock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, l('locked'))
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allskin = json.load(f)
            for item in allskin['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type']['value'] == 'outfit':
                    if 'banner' not in item['id']:
                        await client.party.me.set_outfit(item['id'])
                    else:
                        await client.party.me.set_outfit(item['id'],variants=client.party.me.create_variants(profile_banner='ProfileBanner'))
                    await asyncio.sleep(2)
            else:
                await reply(message, l('all_end', l('outfit')))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['allbackpack'].split(','):
        try:
            flag = False
            if client.backpacklock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, l('locked'))
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allskin = json.load(f)
            for item in allskin['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type']['value'] == 'backpack':
                    if 'banner' not in item['id']:
                        await client.party.me.set_backpack(item['id'])
                    else:
                        await client.party.me.set_backpack(item['id'],variants=client.party.me.create_variants(profile_banner='ProfileBanner'))
                    await asyncio.sleep(2)
            else:
                await reply(message, l('all_end', l('backpack')))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['allpet'].split(','):
        try:
            flag = False
            if client.backpacklock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, l('locked'))
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allskin = json.load(f)
            for item in allskin['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type']['value'] == 'pet':
                    if 'banner' not in item['id']:
                        await client.party.me.set_backpack(item['id'])
                    else:
                        await client.party.me.set_backpack(item['id'],variants=client.party.me.create_variants(profile_banner='ProfileBanner'))
                    await asyncio.sleep(2)
            else:
                await reply(message, l('all_end', l('pet')))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['allpickaxe'].split(','):
        try:
            flag = False
            if client.pickaxelock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, l('locked'))
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allskin = json.load(f)
            for item in allskin['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type']['value'] == 'pickaxe':
                    if 'banner' not in item['id']:
                        await client.party.me.set_pickaxe(item['id'])
                    else:
                        await client.party.me.set_pickaxe(item['id'],variants=client.party.me.create_variants(profile_banner='ProfileBanner'))
                    await asyncio.sleep(2)
            else:
                await reply(message, l('all_end', l('pickaxe')))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['allemote'].split(','):
        try:
            flag = False
            if client.emotelock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, l('locked'))
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allemote = json.load(f)
            for item in allemote['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type']['value'] == 'emote':
                    await client.party.me.set_emote(item['id'])
                    await asyncio.sleep(5)
            else:
                await reply(message, l('all_end', l('emote')))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['allemoji'].split(','):
        try:
            flag = False
            if client.emotelock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, l('locked'))
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allemote = json.load(f)
            for item in allemote['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type']['value'] == 'emoji':
                    await client.party.me.set_emote(item['id'])
                    await asyncio.sleep(5)
            else:
                await reply(message, l('all_end', l('emoji')))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['alltoy'].split(','):
        try:
            flag = False
            if client.emotelock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, l('locked'))
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allemote = json.load(f)
            for item in allemote['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type']['value'] == 'toy':
                    await client.party.me.set_emote(item['id'])
                    await asyncio.sleep(5)
            else:
                await reply(message, l('all_end', l('toy')))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['setenlightenment'].split(','):
        try:
            if await change_asset(client, message.author.id, "outfit", client.party.me.outfit, client.party.me.outfit_variants,(args[1],args[2])) is True:
                await reply(message, l('set_to', 'enlightenment', f'{args[1]}, {args[2]}'))
            else:
                await reply(message, l('locked'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_changing_asset'))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['setenlightenment']}] [{l('number')}] [{l('number')}]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif True in [args[0] in commands[key].split(',') for key in ("cid", "bid", "petcarrier", "pickaxe_id", "eid", "emoji_id", "toy_id", "id")]:
        type_ = convert_to_type(args[0])
        if rawcontent == '':
            await reply(message, f"[{commands[type_]}] [ID]")
            return
        try:
            result = await loop.run_in_executor(None, search_item, data["lang"], "id", rawcontent, type_)
            if result is None:
                result = await loop.run_in_executor(None, search_item, "en", "id", rawcontent, type_)
            if result is None:
                await reply(message, l('item_notfound'))
            else:
                if len(result) > 30:
                    await reply(message, l('too_many_items', str(len(result))))
                    return
                if len(result) == 1:
                    if await change_asset(client, message.author.id, result[0]["type"]["value"], result[0]['id']) is True:
                        await reply(message, f"{result[0]['type']['displayValue']}: {result[0]['name']} | {result[0]['id']}")
                    else:
                        await reply(message, l('locked'))
                else:
                    text = str()
                    for count, item in enumerate(result):
                        text += f"\n{count+1} {item['type']['displayValue']}: {item['name']} | {item['id']}"
                    text += f"\n{l('enter_to_change_asset')}"
                    await reply(message, text)
                    client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{item['type']['value']}', '{item['id']}')" for item in result]}
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_changing_asset'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif True in  [args[0] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe", "emote", "emoji", "toy", "item")]:
        type_ = convert_to_type(args[0])
        if rawcontent == '':
            await reply(message, f"[{commands[type_]}] [{l('itemname')}]")
            return
        try:
            result = await loop.run_in_executor(None, search_item, data["lang"], "name", rawcontent, type_)
            if result is None:
                result = await loop.run_in_executor(None, search_item, "en", "name", rawcontent, type_)
            if result is None:
                await reply(message, l('item_notfound'))
            else:
                if len(result) > 30:
                    await reply(message, l('too_many_items', str(len(result))))
                    return
                if len(result) == 1:
                    if await change_asset(client, message.author.id, result[0]["type"]["value"], result[0]['id']) is True:
                        await reply(message, f"{result[0]['type']['displayValue']}: {result[0]['name']} | {result[0]['id']}")
                    else:
                        await reply(message, l('locked'))
                else:
                    text = str()
                    for count, item in enumerate(result):
                        text += f"\n{count+1} {item['type']['displayValue']}: {item['name']} | {item['id']}"
                    text += f"\n{l('enter_to_change_asset')}"
                    await reply(message, text)
                    client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{item['type']['value']}', '{item['id']}')" for item in result]}
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_changing_asset'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['set'].split(','):
        if rawcontent == '':
            await reply(message, f"[{commands['set']}] [{l('setname')}]")
            return
        try:
            result = await loop.run_in_executor(None, search_item, data["lang"], "set", rawcontent)
            if result is None:
                result = await loop.run_in_executor(None, search_item, "en", "set", rawcontent)
            if result is None:
                await reply(message, l('item_notfound'))
            else:
                if len(result) > 30:
                    await reply(message, l('too_many_items', str(len(result))))
                    return
                if len(result) == 1:
                    if await change_asset(client, message.author.id, result[0]["type"]["value"], result[0]['id']) is True:
                        await reply(message, f"{result[0]['type']['displayValue']}: {result[0]['name']} | {result[0]['id']}({result[0]['set']['value']})")
                    else:
                        await reply(message, l('locked'))
                else:
                    text = str()
                    for count, item in enumerate(result):
                        text += f"\n{count+1} {item['type']['displayValue']}: {item['name']} | {item['id']}({result[0]['set']['value']})"
                    text += f"\n{l('enter_to_change_asset')}"
                    await reply(message, text)
                    client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{item['type']['value']}', '{item['id']}')" for item in result]}
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_changing_asset'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['setstyle'].split(','):
        try:
            if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe")]:
                await reply(message, f"[{commands['setstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                return
            type_ = convert_to_type(args[1])
            id_ = member_asset(client.party.me, convert_to_asset(args[1]))
            result = search_style(data["lang"], id_)
            if result is None:
                await reply(message, l('no_stylechange'))
            else:
                text = str()
                for count, item in enumerate(result):
                    text += f"\n{count+1} {item['name']}"
                text += f"\n{l('enter_to_set_style')}"
                await reply(message, text)
                client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{type_}', '{id_}', {variants['variants']})" for variants in result]}
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['setstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['addstyle'].split(','):
        try:
            if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe")]:
                await reply(message, f"[{commands['addstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                return
            type_ = convert_to_type(args[1])
            id_ = member_asset(client.party.me, convert_to_asset(args[1]))
            variants_ = eval(f"client.party.me.{convert_to_asset(args[1])}_variants")
            result = search_style(data["lang"], id_)
            if result is None:
                await reply(message, l('no_stylechange'))
            else:
                text = str()
                for count, item in enumerate(result):
                    text += f"\n{count+1} {item['name']}"
                text += f"\n{l('enter_to_set_style')}"
                await reply(message, text)
                client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{type_}', '{id_}', {variants_} + {variants['variants']})" for variants in result]}
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['addstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['setvariant'].split(','):
        try:
            if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe")]:
                await reply(message, f"[{commands['setvariant']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                return
            variantdict={}
            for count,text in enumerate(args[2:]):
                if count % 2 != 0:
                    continue
                try:
                    variantdict[text]=args[count+3]
                except IndexError:
                    break
            type_ = convert_to_type(args[1])
            id_ = member_asset(client.party.me, convert_to_asset(args[1]))
            variants = client.party.me.create_variants(item='AthenaCharacter',**variantdict)
            print(variants)
            if await change_asset(client, message.author.id, type_, id_, variants, client.party.me.enlightenments) is False:
                await reply(message, l('locked'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_changing_asset'))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['setvariant']}] [ID] [variant] [{l('number')}]")
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['addvariant'].split(','):
        try:
            if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe")]:
                await reply(message, f"[{commands['addvariant']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                return
            variantdict={}
            for count,text in enumerate(args[2:]):
                if count % 2 != 0:
                    continue
                try:
                    variantdict[text]=args[count+3]
                except IndexError:
                    break
            type_ = convert_to_type(args[1])
            id_ = member_asset(client.party.me, convert_to_asset(args[1]))
            variants = client.party.me.create_variants(item='AthenaCharacter',**variantdict)
            variants += eval(f"client.party.me.{convert_to_asset(args[1])}_variants")
            if await change_asset(client, message.author.id, type_, id_, variants, client.party.me.enlightenments) is False:
                await reply(message, l('locked'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_changing_asset'))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['addvariant']}] [ID] [variant] [{l('number')}]")
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif True in [args[0] in commands[key].split(',') for key in ("outfitasset", "backpackasset", "pickaxeasset", "emoteasset")]:
        type_ = convert_to_type(args[0])
        try:
            if rawcontent == '':
                await reply(message, f"[{commands[f'{type_}asset']}] [{l('assetpath')}]")
                return
            if await change_asset(client, message.author.id, type_, rawcontent) is False:
                await reply(message, l('locked'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_changing_asset'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif True in [args[0].lower().startswith(id_) for id_ in ("cid_", "bid_", "petcarrier_", "pickaxe_id_", "eid_", "emoji_", "toy_")]:
        try:
            type_ = convert_to_type("_".join(args[0].split('_')[:-1]) + "_")
            if await change_asset(client, message.author.id, type_, args[0]) is False:
                await reply(message, l('locked'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_changing_asset'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0].lower().startswith('playlist_'):
        try:
            await client.party.set_playlist(args[0])
            await reply(message, l('set_playlist', args[0]))
            data['fortnite']['playlist']=args[0]
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('not_party_leader'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    else:
        if ': ' in message.content:
            return
        if args[0].isdigit() and client.select.get(message.author.id) is not None:
            try:
                if int(args[0]) == 0:
                    await reply(message, l('please_enter_valid_number'))
                    return
                exec_ = client.select[message.author.id]["exec"][int(args[0])-1]
                variable=globals()
                variable.update(locals())
                if client.select[message.author.id].get("variable") is not None:
                    variable.update(client.select[message.author.id]["variable"][int(args[0])-1])
                await aexec(exec_, variable)
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('please_enter_valid_number'))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))
        else:
            result = await loop.run_in_executor(None, search_item, data["lang"], "name", content, "item")
            if result is None:
                result = await loop.run_in_executor(None, search_item, "en", "name", content, "item")
            if result is not None:
                if len(result) > 30:
                    await reply(message, l('too_many_items', str(len(result))))
                    return
                if len(result) == 1:
                    if await change_asset(client, message.author.id, result[0]["type"]["value"], result[0]['id']) is True:
                        await reply(message, f"{result[0]['type']['displayValue']}: {result[0]['name']} | {result[0]['id']}")
                    else:
                        await reply(message, l('locked'))
                else:
                    text = str()
                    for count, item in enumerate(result):
                        text += f"\n{count+1} {item['type']['displayValue']}: {item['name']} | {item['id']}"
                    text += f"\n{l('enter_to_change_asset')}"
                    await reply(message, text)
                    client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{item['type']['value']}', '{item['id']}')" for item in result]}

#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================

async def event_party_message(message: fortnitepy.PartyMessage) -> None:
    global blacklist
    global whitelist
    global otherbotlist
    global blacklist_
    global whitelist_
    global kill
    if message is None:
        return
    client=message.client
    if data['discord']['enabled'] is True and dclient.isready is False:
        return
    if client.isready is False:
        return
    name=client.user.display_name
    author_id = message.author.id
    loop = asyncio.get_event_loop()
    add_cache(client, message.author)
    if message.author.id in blacklist and data['fortnite']['blacklist-ignorecommand'] is True:
        return
    if message.author.id in otherbotlist and data['fortnite']['ignorebot'] is True:
        return
    if not client.owner is None:
        if client.partychat is False:
            if client.partychatperfect is True:
                return
            elif not message.author.id == client.owner.id:
                return
    else:
        if client.partychat is False:
            return
    content=message.content
    if data['caseinsensitive'] is True:
        args = jaconv.kata2hira(content.lower()).split()
    else:
        args = content.split()
    rawargs = content.split()
    rawcontent = ' '.join(rawargs[1:])
    rawcontent2 = ' '.join(rawargs[2:])
    user=None
    if rawcontent in commands['me'].split(','):
        rawcontent=str(message.author.display_name)
    client_user_display_name=name
    member_joined_at_most=[client.user.id, client.party.me.joined_at]
    for member_ in client.party.members.values():
        add_cache(client, member_)
        try:
            if member_joined_at_most != []:
                if member_.id in [i.user.id for i in loadedclients]:
                    if member_.id != client.user.id:
                        client_user_display_name+=f"/{str(member_.display_name)}"
                    if member_.joined_at < member_joined_at_most[1]:
                        member_joined_at_most=[member_.id, member_.joined_at]
            else:
                member_joined_at_most=[client.user.id, client.party.me.joined_at]
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
    if client.user.id == member_joined_at_most[0]:
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(f'[{now_()}] [{l("party")}] [{client_user_display_name}] {message.author.display_name} | {content}')
            dstore(message.author.display_name,f'[{client_user_display_name}] [{l("party")}] {content}')
        else:
            if data['no-logs'] is False:
                print(f'[{now_()}] [{l("party")}/{client.party.id}] [{client_user_display_name}] {message.author.display_name} / {message.author.id} [{platform_to_str(message.author.platform)}/{message.author.input}] | {content}')
            dstore(f'{message.author.display_name} / {message.author.id} [{platform_to_str(message.author.platform)}/{message.author.input}]',f'[{client_user_display_name}] [{l("party")}/{client.party.id}] {content}')

    flag = False
    if isinstance(message, fortnitepy.message.MessageBase) is True:
        if client.owner is not None:
            if data['fortnite']['whitelist-ownercommand'] is True:
                if client.owner.id != message.author.id and message.author.id not in whitelist:
                    flag = True
            else:
                if client.owner.id != message.author.id:
                    flag = True
        else:
            if data['fortnite']['whitelist-ownercommand'] is True:
                if message.author.id not in whitelist:
                    flag = True
            else:
                flag = True
    else:
        if dclient.owner is not None:
            if data['discord']['whitelist-ownercommand'] is True:
                if client.owner.id != message.author.id and message.author.id not in whitelist_:
                    flag = True
            else:
                if client.owner.id != message.author.id:
                    flag = True
        else:
            if data['discord']['whitelist-ownercommand'] is True:
                if message.author.id not in whitelist_:
                    flag = True
            else:
                flag = True
    if flag is True:
        for checks in commands.items():
            if checks[0] in ignore:
                continue
            if commands['ownercommands'] == '':
                break
            for command in commands['ownercommands'].split(','):
                if args[0] in commands[command.lower()].split(','):
                    await reply(message, l("this_command_owneronly"))
                    return

    if args[0] in commands['prev'].split(','):
        if client.prevmessage.get(message.author.id) is None:
            client.prevmessage[message.author.id]='None'
        content=client.prevmessage.get(message.author.id)
        if data['caseinsensitive'] is True:
            args = jaconv.kata2hira(content.lower()).split()
        else:
            args = content.split()
        args = jaconv.kata2hira(content.lower()).split()
        rawargs = content.split()
        rawcontent = ' '.join(rawargs[1:])
        rawcontent2 = ' '.join(rawargs[2:])
    client.prevmessage[message.author.id]=content

    for key,value in replies.items():
        if args[0] in key.split(','):
            try:
                await reply(message, value)
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))
            return

    if data['discord']['enabled'] is True and dclient.isready is True:
        if args[0] in commands['addblacklist_discord'].split(','):
            try:
                if rawcontent == '' or args[1].isdigit() is False:
                    await reply(message, f"[{commands['addblacklist_discord']}] [{l('userid')}]")
                    return
                user = dclient.get_user(int(args[1]))
                if user is None:
                    user = await dclient.fetch_user(int(args[1]))
                if user.id not in blacklist_:
                    blacklist_.append(user.id)
                    data["discord"]["blacklist"].append(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["discord"]["blacklist"] = data["discord"]["blacklist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, l('add_to_list', f'{str(user)} / {str(user.id)}', l('discord_blacklist')))
                else:
                    await reply(message, l('already_list', f'{str(user)} / {user.id}', l('discord_blacklist')))
            except discord.NotFound:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('user_notfound'))
            except discord.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
                dstore(name,f'>>> {l("error_while_requesting_userinfo")}')
                await reply(message, l("error_while_requesting_userinfo"))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['removeblacklist_discord'].split(','):
            try:
                if rawcontent == '' or args[1].isdigit() is False:
                    await reply(message, f"[{commands['removeblacklist_discord']}] [{l('userid')}]")
                    return
                user = dclient.get_user(int(args[1]))
                if user is None:
                    user = await dclient.fetch_user(int(args[1]))
                if user.id in blacklist_:
                    blacklist_.remove(user.id)
                    data["discord"]["blacklist"].remove(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["discord"]["blacklist"] = data["discord"]["blacklist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, l('remove_from_list', f'{str(user)} / {user.id}', l('discord_blacklist')))
                else:
                    await reply(message, l('not_list', f'{str(user)} / {user.id}', l('discord_blacklist')))
            except discord.NotFound:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('user_notfound'))
            except discord.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
                dstore(name,f'>>> {l("error_while_requesting_userinfo")}')
                await reply(message, l("error_while_requesting_userinfo"))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['addwhitelist_discord'].split(','):
            try:
                if rawcontent == '' or args[1].isdigit() is False:
                    await reply(message, f"[{commands['addwhitelist_discord']}] [{l('userid')}]")
                    return
                user = dclient.get_user(int(args[1]))
                if user is None:
                    user = await dclient.fetch_user(int(args[1]))
                if user.id not in whitelist_:
                    whitelist_.append(user.id)
                    data["discord"]["whitelist"].append(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["discord"]["whitelist"] = data["discord"]["whitelist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, l('add_from_list', f'{str(user)} / {user.id}', l('discord_whitelist')))
                else:
                    await reply(message, l('already_list', f'{str(user)} / {user.id}', l('discord_whitelist')))
            except discord.NotFound:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('user_notfound'))
            except discord.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
                dstore(name,f'>>> {l("error_while_requesting_userinfo")}')
                await reply(message, l("error_while_requesting_userinfo"))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['removewhitelist_discord'].split(','):
            try:
                if rawcontent == '' or args[1].isdigit() is False:
                    await reply(message, f"[{commands['removewhitelist_discord']}] [{l('userid')}]")
                    return
                user = dclient.get_user(int(args[1]))
                if user is None:
                    user = await dclient.fetch_user(int(args[1]))
                if user.id in whitelist_:
                    whitelist_.remove(user.id)
                    data["discord"]["whitelist"].remove(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["discord"]["whitelist"] = data["discord"]["whitelist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, l('remove_list', f'{str(user)} / {user.id}', l('discord_whitelist')))
                else:
                    await reply(message, l('not_list', f'{str(user)} / {user.id}', l('discord_whitelist')))
            except discord.NotFound:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('user_notfound'))
            except discord.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
                dstore(name,f'>>> {l("error_while_requesting_userinfo")}')
                await reply(message, l("error_while_requesting_userinfo"))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

    if args[0] in commands['eval'].split(','):
        try:
            if rawcontent == "":
                await reply(message, f"[{commands['eval']}] [{l('eval')}]")
                return
            variable=globals()
            variable.update(locals())
            if rawcontent.startswith("await "):
                if data['loglevel'] == "debug":
                    print(f"await eval({rawcontent.replace('await ','',1)})")
                result = await eval(rawcontent.replace("await ","",1), variable)
                await reply(message, str(result))
            else:
                if data['loglevel'] == "debug":
                    print(f"eval {rawcontent}")
                result = eval(rawcontent, variable)
                await reply(message, str(result))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"{l('error')}\n{traceback.format_exc()}")

    elif args[0] in commands['exec'].split(','):
        try:
            if rawcontent == "":
                await reply(message, f"[{commands['exec']}] [{l('exec')}]")
                return
            variable=globals()
            variable.update(locals())
            args_=[i.replace("\\nn", "\n") for i in content.replace("\n", "\\nn").split()]
            content_=" ".join(args_[1:])
            result = await aexec(content_, variable)
            await reply(message, str(result))
        except Exception as e:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"{l('error')}\n{traceback.format_exc()}")

    elif args[0] in commands['restart'].split(','):
        try:
            flag = False
            if client.acceptinvite is False:
                if isinstance(message, fortnitepy.message.MessageBase) is True:
                    if client.owner is not None:
                        if data['fortnite']['whitelist-ownercommand'] is True:
                            if client.owner.id != message.author.id and message.author.id not in whitelist:
                                flag = True
                        else:
                            if client.owner.id != message.author.id:
                                flag = True
                    else:
                        if data['fortnite']['whitelist-ownercommand'] is True:
                            if message.author.id not in whitelist:
                                flag = True
                        else:
                            flag = True
                elif isinstance(message, discord.Message) is True:
                    if dclient.owner is not None:
                        if data['discord']['whitelist-ownercommand'] is True:
                            if dclient.owner.id != message.author.id and message.author.id not in whitelist_:
                                flag = True
                        else:
                            if dclient.owner.id != message.author.id:
                                flag = True
                    else:
                        if data['discord']['whitelist-ownercommand'] is True:
                            if message.author.id not in whitelist_:
                                flag = True
                        else:
                            flag = True
            if flag is True:
                await reply(message, l('invite_is_decline'))
                return
            await reply(message, l('restaring'))
            os.chdir(os.getcwd())
            os.execv(os.sys.executable,['python', *sys.argv])
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['relogin'].split(','):
        try:
            flag = False
            if client.acceptinvite is False:
                if isinstance(message, fortnitepy.message.MessageBase) is True:
                    if client.owner is not None:
                        if data['fortnite']['whitelist-ownercommand'] is True:
                            if client.owner.id != message.author.id and message.author.id not in whitelist:
                                flag = True
                        else:
                            if client.owner.id != message.author.id:
                                flag = True
                    else:
                        if data['fortnite']['whitelist-ownercommand'] is True:
                            if message.author.id not in whitelist:
                                flag = True
                        else:
                            flag = True
                elif isinstance(message, discord.Message) is True:
                    if dclient.owner is not None:
                        if data['discord']['whitelist-ownercommand'] is True:
                            if dclient.owner.id != message.author.id and message.author.id not in whitelist_:
                                flag = True
                        else:
                            if dclient.owner.id != message.author.id:
                                flag = True
                    else:
                        if data['discord']['whitelist-ownercommand'] is True:
                            if message.author.id not in whitelist_:
                                flag = True
                        else:
                            flag = True
            if flag is True:
                await reply(message, l('invite_is_decline'))
                return
            await reply(message, l('relogining'))
            await client.restart()
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['reload'].split(','):
        success=reload_configs(client)
        try:
            if success:
                await reply(message, l('success'))
            else:
                await reply(message, l('error'))
                return
            try:
                client.owner=None
                owner=await client.fetch_profile(data['fortnite']['owner'])
                if owner is None:
                    print(red(f'[{now_()}] [{client.user.display_name}] {l("owner_notfound")}'))
                    dstore(client.user.display_name,f'>>> {l("owner_notfound")}')
                else:
                    add_cache(client, owner)
                    client.owner=client.get_friend(owner.id)
                    if client.owner is None:
                        if data['fortnite']['addfriend'] is True:
                            try:
                                await client.add_friend(owner.id)
                            except fortnitepy.HTTPException:
                                if data['loglevel'] == 'debug':
                                    print(red(traceback.format_exc()))
                                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                                if data['loglevel'] == 'normal':
                                    print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_sending_friendrequest")}'))
                                    dstore(client.user.display_name,f'>>> {l("error_while_sending_friendrequest")}')
                                else:
                                    print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_sending_friendrequest")}'))
                                dstore(client.user.display_name,f'>>> {l("error_while_sending_friendrequest")}')
                            except Exception:
                                print(red(traceback.format_exc()))
                                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                        print(red(f'[{now_()}] [{client.user.display_name}] {l("not_friend_with_owner", commands["reload"])}'))
                        dstore(client.user.display_name,f'>>> {l("not_friend_with_owner", commands["reload"])}')
                    else:
                        if data['loglevel'] == 'normal':
                            if data['no-logs'] is False:
                                print(green(f'[{now_()}] [{client.user.display_name}] {l("owner")}: {str(client.owner.display_name)}'))
                            dstore(client.user.display_name,f'{l("owner")}: {str(client.owner.display_name)}')
                        else:
                            if data['no-logs'] is False:
                                print(green(f'[{now_()}] [{client.user.display_name}] {l("owner")}: {str(client.owner.display_name)} / {client.owner.id}'))
                            dstore(client.user.display_name,f'{l("owner")}: {str(client.owner.display_name)} / {client.owner.id}')
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
                dstore(client.user.display_name,f'>>> {l("error_while_requesting_userinfo")}')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

            for blacklistuser in data['fortnite']['blacklist']:
                try:
                    user = await client.fetch_profile(blacklistuser)
                    add_cache(client, user)
                    if user is None:
                        print(red(f'[{now_()}] [{client.user.display_name}] {l("blacklist_user_notfound", blacklistuser)}'))
                        dstore(client.user.display_name,f'>>> {l("blacklist_user_notfound", blacklistuser)}')
                    else:
                        blacklist.append(user.id)
                        if data['loglevel'] == 'debug':
                            print(yellow(f"{str(user.display_name)} / {user.id}"))
                        if data['fortnite']['blacklist-autoblock'] is True:
                            try:
                                await user.block()
                            except Exception:
                                if data['loglevel'] == 'debug':
                                    print(red(traceback.format_exc()))
                                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                    print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
                    dstore(client.user.display_name,f'>>> {l("error_while_requesting_userinfo")}')
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            if data['loglevel'] == "debug":
                print(yellow(blacklist))
            for whitelistuser in data['fortnite']['whitelist']:
                try:
                    user = await client.fetch_profile(whitelistuser)
                    add_cache(client, user)
                    if user is None:
                        print(red(f'[{now_()}] [{client.user.display_name}] {l("whitelist_user_notfound", whitelistuser)}'))
                        dstore(client.user.display_name,f'>>> {l("whitelist_user_notfound", whitelistuser)}')
                    else:
                        whitelist.append(user.id)
                        if data['loglevel'] == 'debug':
                            print(yellow(f"{str(user.display_name)} / {user.id}"))
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                    print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
                    dstore(client.user.display_name,f'>>> {l("error_while_requesting_userinfo")}')
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            if data['loglevel'] == "debug":
                print(yellow(whitelist))

            for invitelistuser in data['fortnite']['invitelist']:
                try:
                    user = await client.fetch_profile(invitelistuser)
                    if user is None:
                        print(red(f'[{now_()}] [{client.user.display_name}] {l("invitelist_user_notfound", invitelistuser)}'))
                        dstore(client.user.display_name,f'>>> {l("invitelist_user_notfound", invitelistuser)}')
                    else:
                        friend = client.get_friend(user.id)
                        if friend is None and user.id != client.user.id:
                            if data['fortnite']['addfriend'] is True:
                                try:
                                    await client.add_friend(friend.id)
                                except fortnitepy.HTTPException:
                                    if data['loglevel'] == 'debug':
                                        print(red(traceback.format_exc()))
                                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                                    if data['loglevel'] == 'normal':
                                        print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_sending_friendrequest")}'))
                                        dstore(client.user.display_name,f'>>> {l("error_while_sending_friendrequest")}')
                                    else:
                                        print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_sending_friendrequest")}'))
                                        dstore(client.user.display_name,f'>>> {l("error_while_sending_friendrequest")}')
                                except Exception:
                                    print(red(traceback.format_exc()))
                                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                            print(red(f'[{now_()}] [{client.user.display_name}] {l("not_friend_with_inviteuser", invitelistuser)}'))
                            dstore(client.user.display_name,f'>>> {l("not_friend_with_inviteuser", invitelistuser)}')
                        else:
                            add_cache(client, user)
                            client.invitelist.append(user.id)
                            if data['loglevel'] == 'debug':
                                print(yellow(f"{str(user.display_name)} / {user.id}"))
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                    print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
                    dstore(client.user.display_name,f'>>> {l("error_while_requesting_userinfo")}')
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
            if data['loglevel'] == "debug":
                print(yellow(client.invitelist))
            if data['discord']['enabled'] is True:
                dclient_user = str(dclient.user)
                activity = discord.Game(name=data['discord']['status'])
                await dclient.change_presence(activity=activity)

                for blacklistuser in data['discord']['blacklist']:
                    user = dclient.get_user(blacklistuser)
                    if user is None:
                        try:
                            user = await dclient.fetch_user(blacklistuser)
                        except discord.NotFound:
                            if data['loglevel'] == "debug":
                                print(red(traceback.format_exc()))
                                dstore(dclient_user,f'>>> {traceback.format_exc()}')
                            user = None
                    if user is None:
                        print(red(f'[{now_()}] [{dclient_user}] {l("discord_blacklist_user_notfound", blacklistuser)}'))
                        dstore(dclient_user,f'>>> {l("discord_blacklist_user_notfound", blacklistuser)}')
                    else:
                        blacklist_.append(user.id)
                        if data['loglevel'] == 'debug':
                            print(yellow(f"{user} / {user.id}"))
                if data['loglevel'] == "debug":
                    print(yellow(blacklist_))
                for whitelistuser in data['discord']['whitelist']:
                    user = dclient.get_user(whitelistuser)
                    if user is None:
                        try:
                            user = await dclient.fetch_user(whitelistuser)
                        except discord.NotFound:
                            if data['loglevel'] == "debug":
                                print(red(traceback.format_exc()))
                                dstore(dclient_user,f'>>> {traceback.format_exc()}')
                            user = None
                    if user is None:
                        print(red(f'[{now_()}] [{dclient_user}] {l("discord_whitelist_user_notfound", whitelistuser)}'))
                        dstore(dclient_user,f'>>> {l("discord_whitelist_user_notfound", whitelistuser)}')
                    else:
                        whitelist_.append(user.id)
                        if data['loglevel'] == 'debug':
                            print(yellow(f"{user.display_name} / {user.id}"))
                if data['loglevel'] == "debug":
                    print(yellow(whitelist_))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['addblacklist'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['addblacklist']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(name) and user.id != client.user.id and user.id not in blacklist}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.id not in blacklist:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if user.id not in blacklist:
                    blacklist.append(user.id)
                    if user.display_name is not None:
                        data["fortnite"]["blacklist"].append(str(user.display_name))
                    else:
                        data["fortnite"]["blacklist"].append(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, l('add_to_list', f'{str(user.display_name)} / {user.id}', l('blacklist')))
                else:
                    await reply(message, l('already_in_list', f'{str(user.display_name)} / {user.id}', l('blacklist')))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
            if user.id not in blacklist:
                blacklist.append(user.id)
                if user.display_name is not None:
                    data["fortnite"]["blacklist"].append(str(user.display_name))
                else:
                    data["fortnite"]["blacklist"].append(user.id)
                try:
                    with open("config.json", "r", encoding="utf-8") as f:
                        data_ = json.load(f)
                except json.decoder.JSONDecodeError:
                    with open("config.json", "r", encoding="utf-8-sig") as f:
                        data_ = json.load(f)
                data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
                with open("config.json", "w", encoding="utf-8") as f:
                    json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                await reply(message, l('add_to_list', f'{str(user.display_name)} / {user.id}', l('blacklist')))
            else:
                await reply(message, l('already_in_list', f'{str(user.display_name)} / {user.id}', l('blacklist')))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_add_to_list', l('blacklist'))}"
                await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['removeblacklist'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['removeblacklist']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and user.id in blacklist}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.id in blacklist:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if user.id in blacklist:
                    blacklist.remove(user.id)
                    try:
                        data["fortnite"]["blacklist"].remove(str(user.display_name))
                    except ValueError:
                        data["fortnite"]["blacklist"].remove(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, l('remove_from_list', f'{str(user.display_name)} / {user.id}', l('blacklist')))
                else:
                    await reply(message, l('not_list', f'{str(user.display_name)} / {user.id}', l('blacklist')))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        if user.id in blacklist:
            blacklist.remove(user.id)
            try:
                data["fortnite"]["blacklist"].remove(str(user.display_name))
            except ValueError:
                data["fortnite"]["blacklist"].remove(user.id)
            try:
                with open("config.json", "r", encoding="utf-8") as f:
                    data_ = json.load(f)
            except json.decoder.JSONDecodeError:
                with open("config.json", "r", encoding="utf-8-sig") as f:
                    data_ = json.load(f)
            data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
            await reply(message, l('remove_from_list', f'{str(user.display_name)} / {user.id}', l('blacklist')))
        else:
            await reply(message, l('not_list', f'{str(user.display_name)} / {user.id}', l('blacklist')))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_remove_from_list', l('blacklist'))}"
                await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['addwhitelist'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['addwhitelist']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and user.id not in whitelist}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.id not in whitelist:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if user.id not in whitelist:
                    whitelist.append(user.id)
                    if user.display_name is not None:
                        data["fortnite"]["whitelist"].append(str(user.display_name))
                    else:
                        data["fortnite"]["whitelist"].append(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["fortnite"]["whitelist"] = data["fortnite"]["whitelist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, l("add_to_list", f"{str(user.display_name)} / {user.id}", l('whitelist')))
                else:
                    await reply(message, l("already_list", f"{str(user.display_name)} / {user.id}", l('whitelist')))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
            if user.id not in whitelist:
                whitelist.append(user.id)
                if user.display_name is not None:
                    data["fortnite"]["whitelist"].append(str(user.display_name))
                else:
                    data["fortnite"]["whitelist"].append(user.id)
                try:
                    with open("config.json", "r", encoding="utf-8") as f:
                        data_ = json.load(f)
                except json.decoder.JSONDecodeError:
                    with open("config.json", "r", encoding="utf-8-sig") as f:
                        data_ = json.load(f)
                data_["fortnite"]["whitelist"] = data["fortnite"]["whitelist"]
                with open("config.json", "w", encoding="utf-8") as f:
                    json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                await reply(message, l("add_to_list", f"{str(user.display_name)} / {user.id}", l('whitelist')))
            else:
                await reply(message, l("already_list", f"{str(user.display_name)} / {user.id}", l('whitelist')))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_add_to_list', l('whitelist'))}"
                await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['removewhitelist'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['removewhitelist']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and user.id in whitelist}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.id in whitelist:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l("too_many_users", str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if user.id in whitelist:
                    whitelist.remove(user.id)
                    try:
                        data["whitelist"].remove(str(user.display_name))
                    except ValueError:
                        data["whitelist"].remove(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["whitelist"] = data["whitelist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, l("remove_from_list", f"{str(user.display_name)} / {user.id}", l('whitelist')))
                else:
                    await reply(message, l("not_list", f"{str(user.display_name)} / {user.id}", l('whitelist')))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        if user.id in whitelist:
            whitelist.remove(user.id)
            try:
                data["whitelist"].remove(str(user.display_name))
            except ValueError:
                data["whitelist"].remove(user.id)
            try:
                with open("config.json", "r", encoding="utf-8") as f:
                    data_ = json.load(f)
            except json.decoder.JSONDecodeError:
                with open("config.json", "r", encoding="utf-8-sig") as f:
                    data_ = json.load(f)
            data_["whitelist"] = data["whitelist"]
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
            await reply(message, l("remove_from_list", f"{str(user.display_name)} / {user.id}", l('whitelist')))
        else:
            await reply(message, l("not_list", f"{str(user.display_name)} / {user.id}", l('whitelist')))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_remove_from_list', l('whitelist'))}"
                await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['addinvitelist'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['addinvitelist']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and user.id not in client.invitelist}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.id not in client.invitelist:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l("too_many_users", str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if user.id not in client.invitelist:
                    client.invitelist.append(user.id)
                    if user.display_name is not None:
                        data["fortnite"]["invitelist"].append(str(user.display_name))
                    else:
                        data["fortnite"]["invitelist"].append(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["fortnite"]["invitelist"] = data["fortnite"]["invitelist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, l("add_to_list", f"{str(user.display_name)} / {user.id}", l('invitelist')))
                else:
                    await reply(message, l("already_list", f"{str(user.display_name)} / {user.id}", l('invitelist')))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        if user.id not in client.invitelist:
            client.invitelist.append(user.id)
            if user.display_name is not None:
                data["fortnite"]["invitelist"].append(str(user.display_name))
            else:
                data["fortnite"]["invitelist"].append(user.id)
            try:
                with open("config.json", "r", encoding="utf-8") as f:
                    data_ = json.load(f)
            except json.decoder.JSONDecodeError:
                with open("config.json", "r", encoding="utf-8-sig") as f:
                    data_ = json.load(f)
            data_["fortnite"]["invitelist"] = data["fortnite"]["invitelist"]
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
            await reply(message, l("add_to_list", f"{str(user.display_name)} / {user.id}", l('invitelist')))
        else:
            await reply(message, l("already_list", f"{str(user.display_name)} / {user.id}", l('invitelist')))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_add_to_list', l('invitelist'))}"
                await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['removeinvitelist'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['removeinvitelist']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and user.id in client.invitelist}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if user.id in client.invitelist:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l("too_many_users", str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if user.id in client.invitelist:
                    client.invitelist.remove(user.id)
                    try:
                        data["fortnite"]["invitelist"].remove(str(user.display_name))
                    except ValueError:
                        data["fortnite"]["invitelist"].remove(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["fortnite"]["invitelist"] = data["fortnite"]["invitelist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, l("remove_from_list", f"{str(user.display_name)} / {user.id}", l('invitelist')))
                else:
                    await reply(message, l("not_list", f"{str(user.display_name)} / {user.id}", l('invitelist')))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        if user.id in client.invitelist:
            client.invitelist.remove(user.id)
            try:
                data["fortnite"]["invitelist"].remove(str(user.display_name))
            except ValueError:
                data["fortnite"]["invitelist"].remove(user.id)
            try:
                with open("config.json", "r", encoding="utf-8") as f:
                    data_ = json.load(f)
            except json.decoder.JSONDecodeError:
                with open("config.json", "r", encoding="utf-8-sig") as f:
                    data_ = json.load(f)
            data_["fortnite"]["invitelist"] = data["fortnite"]["invitelist"]
            with open("config.json", "w", encoding="utf-8") as f:
                json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
            await reply(message, l("remove_from_list", f"{str(user.display_name)} / {user.id}", l('invitelist')))
        else:
            await reply(message, l("not_list", f"{str(user.display_name)} / {user.id}", l('invitelist')))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_remove_from_list', l('invitelist'))}"
                await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['get'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['get']}] [{l('name_or_id')}]")
                return
            users = {str(member.display_name): member for member in client.party.members.values() if rawcontent in str(member.display_name)}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.party.members.get(user.id) is not None:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l("too_many_users", str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                member=client.party.members.get(user.id)
                if member is None:
                    await reply(message, l("user_not_in_party"))
                    return
                if data['no-logs'] is False:
                    print(f'{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}')
                if data['loglevel'] == 'debug':
                    print(json.dumps(member.meta.schema, indent=2))
                dstore(name,f'{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}')
                await reply(message, f'{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}')
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        member=client.party.members.get(user.id)
        if member is None:
            await reply(message, l("user_not_in_party"))
            return
        if data['no-logs'] is False:
            print(f'''{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}''')
        if data['loglevel'] == 'debug':
            print(json.dumps(member.meta.schema, indent=2))
        dstore(name,f'''{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}''')
        await reply(message, f'''{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}''')""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_get_userinfo')}"
                await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['friendcount'].split(','):
        try:
            if data['no-logs'] is False:
                print(f"{l('friendcount')}: {len(client.friends)}")
            dstore(name,f"{l('friendcount')}: {len(client.friends)}")
            await reply(message, f"{l('friendcount')}: {len(client.friends)}")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['pendingcount'].split(','):
        try:
            outbound = []
            inbound = []
            for pending in client.pending_friends.values():
                if pending.direction == 'OUTBOUND':
                    outbound.append(pending)
                elif pending.direction == 'INBOUND':
                    inbound.append(pending)
            if data['no-logs'] is False:
                print(f"{l('pendingcount')}: {len(client.pending_friends)}\n{l('outbound')}: {len(outbound)}\n{l('inbound')}: {len(inbound)}")
            dstore(name,f"{l('pendingcount')}: {len(client.pending_friends)}\n{l('outbound')}: {len(outbound)}\n{l('inbound')}: {len(inbound)}")
            await reply(message, f"{l('pendingcount')}: {len(client.pending_friends)}\n{l('outbound')}: {len(outbound)}\n{l('inbound')}: {len(inbound)}")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['blockcount'].split(','):
        try:
            if data['no-logs'] is False:
                print(f"{l('blockcount')}: {len(client.blocked_users)}")
            dstore(name,f"{l('blockcount')}: {len(client.blocked_users)}")
            await reply(message, f"{l('blockcount')}: {len(client.blocked_users)}")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['friendlist'].split(','):
        try:
            text=''
            for friend in client.friends.values():
                add_cache(client, friend)
                text+=f'\n{str(friend.display_name)}'
            if data['no-logs'] is False:
                print(f'{text}')
            dstore(name,f'{text}')
            await reply(message, f'{text}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['pendinglist'].split(','):
        try:
            outbound=''
            inbound=''
            for pending in client.pending_friends.values():
                add_cache(client, pending)
                if pending.direction == 'OUTBOUND':
                    outbound+=f'\n{str(pending.display_name)}'
                elif pending.direction == 'INBOUND':
                    inbound+=f'\n{str(pending.display_name)}'
            if data['no-logs'] is False:
                print(f"{l('outbound')}: {outbound}\n{l('inbound')}: {inbound}")
            dstore(name,f"{l('outbound')}: {outbound}\n{l('inbound')}: {inbound}")
            await reply(message, f"{l('outbound')}: {outbound}\n{l('inbound')}: {inbound}")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['blocklist'].split(','):
        try:
            text=''
            for block in client.blocked_users.values():
                add_cache(client, block)
                text+=f'\n{str(block.display_name)}'
            if data['no-logs'] is False:
                print(f'{text}')
            dstore(name,f'{text}')
            await reply(message, f'{text}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['outfitmimic'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.outfitmimic=True
                await reply(message, l('set_to', l('mimic', l('outfit')), l('on')))
            elif args[1] in commands['false'].split(','):
                client.outfitmimic=False
                await reply(message, l('set_to', l('mimic', l('outfit')), l('off')))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['skinmimic']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['backpackmimic'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.backpackmimic=True
                await reply(message, l('mimic_set', l('set_to', l('mimic', l('backpack')), l('on'))))
            elif args[1] in commands['false'].split(','):
                client.backpackmimic=False
                await reply(message, l('mimic_set', l('set_to', l('mimic', l('backpack')), l('off'))))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['skinmimic']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['pickaxemimic'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.pickaxemimic=True
                await reply(message, l('mimic_set', l('set_to', l('mimic', l('pickaxe')), l('on'))))
            elif args[1] in commands['false'].split(','):
                client.pickaxemimic=False
                await reply(message, l('mimic_set', l('set_to', l('mimic', l('pickaxe')), l('off'))))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['skinmimic']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['emotemimic'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.emotemimic=True
                await reply(message, l('mimic_set', l('set_to', l('mimic', l('emote')), l('on'))))
            elif args[1] in commands['false'].split(','):
                client.emotemimic=False
                await reply(message, l('mimic_set', l('set_to', l('mimic', l('emote')), l('off'))))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['emotemimic']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['whisper'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.whisper=True
                await reply(message, l('set_to', l('command_from', l('whisper'), l('on'))))
            elif args[1] in commands['false'].split(','):
                client.whisper=False
                await reply(message, l('set_to', l('command_from', l('whisper'), l('off'))))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['whisper']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['partychat'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.partychat=True
                await reply(message, l('set_to', l('command_from', l('partychat'), l('on'))))
            elif args[1] in commands['false'].split(','):
                client.partychat=False
                await reply(message, l('set_to', l('command_from', l('partychat'), l('off'))))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['party']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['discord'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.discord=True
                await reply(message, l('set_to', l('command_from', l('discord'), l('on'))))
            elif args[1] in commands['false'].split(','):
                client.discord=False
                await reply(message, l('set_to', l('command_from', l('discord'), l('off'))))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['discord']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['disablewhisperperfectly'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.whisperperfect=True
                await reply(message, l('set_to', l('disable_perfect', l('whisper'), l('on'))))
            elif args[1] in commands['false'].split(','):
                client.whisperperfect=False
                await reply(message, l('set_to', l('disable_perfect', l('whisper'), l('off'))))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['disablewhisperperfectly']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['disablepartychatperfectly'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.partychatperfect=True
                await reply(message, l('set_to', l('disable_perfect', l('partychat'), l('on'))))
            elif args[1] in commands['false'].split(','):
                client.partychatperfect=False
                await reply(message, l('set_to', l('disable_perfect', l('partychat'), l('on'))))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['disablepartychatperfectly']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['disablediscordperfectly'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.discordperfect=True
                await reply(message, l('set_to', l('disable_perfect', l('discord'), l('on'))))
            elif args[1] in commands['false'].split(','):
                client.discordperfect=False
                await reply(message, l('set_to', l('disable_perfect', l('discord'), l('on'))))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['disablediscordperfectly']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['acceptinvite'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.acceptinvite=True
                await reply(message, l('set_to', l('invite'), l('accept')))
            elif args[1] in commands['false'].split(','):
                client.acceptinvite=False
                await reply(message, l('set_to', l('invite'), l('decline')))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['acceptinvite']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['acceptfriend'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.acceptfriend=True
                await reply(message, l('set_to', l('friendrequest'), l('accept')))
            elif args[1] in commands['false'].split(','):
                client.acceptfriend=False
                await reply(message, l('set_to', l('friendrequest'), l('decline')))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['acceptfriend']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['joinmessageenable'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.joinmessageenable=True
                await reply(message, l('set_to', l('join_', l('message')), l('on')))
            elif args[1] in commands['false'].split(','):
                client.joinmessageenable=False
                await reply(message, l('set_to', l('join_', l('message')), l('off')))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['joinmessageenable']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['randommessageenable'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.randommessageenable=True
                await reply(message, l('set_to', l('join_', l('randommessage')), l('on')))
            elif args[1] in commands['false'].split(','):
                client.randommessageenable=False
                await reply(message, l('set_to', l('join_', l('randommessage')), l('off')))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['randommessageenable']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['wait'].split(','):
        try:
            if client.owner is None:
                client.acceptinvite=False
                try:
                    client.timer_.cancel()
                except AttributeError:
                    pass
                client.timer_=Timer(data['fortnite']['waitinterval'], inviteaccept, [client])
                client.timer_.start()
                await reply(message, l('decline_invite_for', str(data['fortnite']['waitinterval'])))
            else:
                if client.owner.id in client.party.members.keys() and message.author.id != client.owner.id:
                    await reply(message, l('not_available'))
                    return
                client.acceptinvite=False
                try:
                    client.timer_.cancel()
                except AttributeError:
                    pass
                client.timer_=Timer(data['fortnite']['waitinterval'], inviteaccept, [client])
                client.timer_.start()
                await reply(message, l('decline_invite_for', str(data['fortnite']['waitinterval'])))
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['join'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['join']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.has_friend(user.id) is True:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                friend=client.get_friend(user.id)
                if friend is None:
                    await reply(message, l('not_friend_with_user'))
                else:
                    await friend.join_party()
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            friend=client.get_friend(user.id)
            if friend is None:
                await reply(message, l('not_friend_with_user'))
            else:
                await friend.join_party()
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('party_full_or_already_or_offline'))
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('party_notfound'))
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('party_private'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_joining_to_party'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"{l('enter_join_party')}"
                await reply(message, text)
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('party_full_or_already_or_offline'))
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('party_notfound'))
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('party_private'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_joining_to_party'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['joinid'].split(','):
        try:
            await client.join_to_party(party_id=args[1])
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('party_full_or_already'))
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('party_notfound'))
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('party_private'))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['join']}] [{l('party_id')}]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['leave'].split(','):
        try:
            await client.party.me.leave()
            await reply(message, l('party_leave', client.user.party.id))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_leaving_party'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['invite'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['invite']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.has_friend(user.id) is True:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                friend=client.get_friend(user.id)
                if friend is None:
                    await reply(message, l('not_friend_with_user'))
                    return
                await friend.invite()
                await reply(message, l('user_invited', f'{str(friend.display_name)} / {friend.id}', client.party.id))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            friend=client.get_friend(user.id)
            if friend is None:
                await reply(message, l('not_friend_with_user'))
                return
            await friend.invite()
            await reply(message, l('user_invited', f'{str(friend.display_name)} / {friend.id}', client.party.id))
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('party_full_or_already'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_sending_partyinvite'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_invite_user')}"
                await reply(message, text)
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('party_full_or_already'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_sending_partyinvite'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['inviteall'].split(','):
        try:
            for inviteuser in client.invitelist:
                if inviteuser != client.user.id and inviteuser not in client.party.members:
                    try:
                        await client.party.invite(inviteuser)
                    except fortnitepy.PartyError:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(name,f'>>> {traceback.format_exc()}')
                        await reply(message, l('party_full_or_already'))
                    except fortnitepy.Forbidden:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(name,f'>>> {traceback.format_exc()}')
                        await reply(message, l('not_friend_with_user'))
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(name,f'>>> {traceback.format_exc()}')
                        await reply(message, l('error_while_sending_partyinvite'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['message'].split(','):
        try:
            send=rawcontent.split(' : ')
            users = {str(user.display_name): user for user in cache_users.values() if send[0] in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is True}
            try:
                user=await client.fetch_profile(send[0])
                if user is not None:
                    if client.has_friend(user.id) is True:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                friend=client.get_friend(user.id)
                if friend is None:
                    await reply(message, l('not_friend_with_user'))
                    return
                await friend.send(send[1])
                await reply(message, l('user_sent', f'{str(friend.display_name)} / {friend.id}', send[1]))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            friend=client.get_friend(user.id)
            if friend is None:
                await reply(message, l('not_friend_with_user'))
                return
            await friend.send(send[1])
            await reply(message, l('user_sent', f'{str(friend.display_name)} / {friend.id}', send[1]))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l("error_while_requesting_userinfo"))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user, "send": send} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_send')}"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l("error_while_requesting_userinfo"))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['message']}] [{l('name_or_id')}] : [{l('content')}]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['partymessage'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['partymessage']}] [{l('content')}]")
                return
            await client.party.send(rawcontent)
            await reply(message, l('party_sent', client.party.id, rawcontent))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['status'].split(','):
        try:
            await client.set_status(rawcontent)
            await reply(message, l('set_to', l('status'), rawcontent))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['status']}] [{l('content')}]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['banner'].split(','):
        try:
            await client.party.me.edit_and_keep(partial(client.party.me.set_banner,args[1],args[2],client.party.me.banner[2]))
            await reply(message, l('set_to', l('banner'), f"{args[1]}, {args[2]}"))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_changing_asset'))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['banner']}] [{l('bannerid')}] [{l('color')}]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['level'].split(','):
        try:
            await client.party.me.edit_and_keep(partial(client.party.me.set_banner,client.party.me.banner[0],client.party.me.banner[1],int(args[1])))
            await reply(message, l('level', args[1]))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_changing_asset'))
        except ValueError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('must_be_int'))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['level']}] [{l('level')}]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['bp'].split(','):
        try:
            await client.party.me.edit_and_keep(partial(client.party.me.set_battlepass_info,True,args[1],args[2],args[3]))
            await reply(message, l('set_to', l('bpinfo'), f"{l('tier')}: {args[1]}, {l('xpboost')}: {args[2]}, {l('friendxpboost')}: {args[3]}"))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_changing_bpinfo'))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['bp']}] [{l('tier')}] [{l('xpboost')}] [{l('friendxpboost')}]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['privacy'].split(','):
        try:
            if args[1] in commands['privacy_public'].split(','):
                await client.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)
                await reply(message, l('set_to', l('privacy'), l('public')))
            elif args[1] in commands['privacy_friends_allow_friends_of_friends'].split(','):
                await client.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS_ALLOW_FRIENDS_OF_FRIENDS)
                await reply(message, l('set_to', l('privacy'), l('friends_allow_friends_of_friends')))
            elif args[1] in commands['privacy_friends'].split(','):
                await client.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS)
                await reply(message, l('set_to', l('privacy'), l('friends')))
            elif args[1] in commands['privacy_private_allow_friends_of_friends'].split(','):
                await client.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE_ALLOW_FRIENDS_OF_FRIENDS)
                await reply(message, l('set_to', l('privacy'), l('private_allow_friends_of_friends')))
            elif args[1] in commands['privacy_private'].split(','):
                await client.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE)
                await reply(message, l('set_to', l('privacy'), l('private')))
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('not_party_leader'))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['privacy']}] [[{commands['privacy_public']}] / [{commands['privacy_friends_allow_friends_of_friends']}] / [{commands['privacy_friends']}] / [{commands['privacy_private_allow_friends_of_friends']}] / [{commands['privacy_private']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error')) 

    elif args[0] in commands['getuser'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['getuser']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    users[str(user.display_name)] = user
                    add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            text = str()
            for user in users.values():
                text += f'\n{str(user.display_name)} / {user.id}'
            if data['no-logs'] is False:
                print(text)
            dstore(name,text)
            await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['getfriend'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['getfriend']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.has_friend(user.id) is True:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            text = str()
            for user in users.values():
                friend=client.get_friend(user.id)
                if friend is None:
                    continue
                if friend.nickname is None:
                    text += f'\n{str(friend.display_name)} / {friend.id}'
                else:
                    text += f'\n{friend.nickname}({str(friend.display_name)}) / {friend.id}'
                if friend.last_logout is not None:
                    text += "\n{1}: {0.year}/{0.month}/{0.day} {0.hour}:{0.minute}:{0.second}".format(friend.last_logout, l('lastlogin'))
            if data['no-logs'] is False:
                print(text)
            dstore(name,text)
            await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['getpending'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['getpending']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.is_pending(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.is_pending(user.id) is True:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            text = str()
            for user in users.values():
                pending = client.get_pending_friend(user.id)
                if pending is None:
                    continue
                text += f'\n{str(pending.display_name)} / {pending.id}'
            if data['no-logs'] is False:
                print(text)
            dstore(name,text)
            await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['getblock'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['getblock']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.is_blocked(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.is_blocked(user.id) is True:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            text = str()
            for user in users.values():
                block=client.get_blocked_user(user.id)
                if block is None:
                    continue
                text += f'\n{str(block.display_name)} / {block.id}'
            if data['no-logs'] is False:
                print(text)
            dstore(name,text)
            await reply(message, text)
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['info'].split(','):
        try:
            if args[1] in commands['info_party'].split(','):
                text = str()
                text += f"{client.party.id}\n{l('member_count')}: {client.party.member_count}"
                for member in client.party.members.values():
                    add_cache(client, member)
                    if data['loglevel'] == 'normal':
                        text += f'\n{str(member.display_name)}'
                    else:
                        text += f'\n{str(member.display_name)} / {member.id}'
                print(text)
                dstore(None, text)
                await reply(message, text)
                if data['loglevel'] == 'debug':
                    print(json.dumps(client.party.meta.schema, indent=2))
            
            elif True in [args[1] in commands[key].split(',') for key in ("cid", "bid", "petcarrier", "pickaxe_id", "eid", "emoji_id", "toy_id", "id")]:
                type_ = convert_to_type(args[1])
                if rawcontent2 == '':
                    await reply(message, f"[{commands[type_]}] [ID]")
                    return
                result = await loop.run_in_executor(None, search_item, data["lang"], "id", rawcontent2, type_)
                if result is None:
                    result = await loop.run_in_executor(None, search_item, "en", "id", rawcontent2, type_)
                if result is None:
                    await reply(message, l('item_notfound'))
                else:
                    if len(result) > 30:
                        await reply(message, l('too_many_items', str(len(result))))
                        return
                    if len(result) == 1:
                        await reply(message, f"{result[0]['type']['displayValue']}: {result[0]['name']} | {result[0]['id']}\n{result[0]['description']}\{result[0]['rarity']['displayValue']}\n{result[0]['set']['value']}")
                    else:
                        text = str()
                        for count, item in enumerate(result):
                            text += f"\n{count+1} {item['type']['displayValue']}: {item['name']} | {item['id']}"
                        text += f"\n{l('enter_to_show_info')}"
                        await reply(message, text)
                        client.select[message.author.id] = {"exec": [f"await reply(message, f'''{item['type']['displayValue']}: {item['name']} | {item['id']}\n{item['description']}\n{item['rarity']['displayValue']}\n{item['set']['value']}''')" for item in result]}

            elif True in  [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe", "emote", "emoji", "toy", "item")]:
                type_ = convert_to_type(args[1])
                if rawcontent2 == '':
                    await reply(message, f"[{commands[type_]}] [{l('itemname')}]")
                    return
                result = await loop.run_in_executor(None, search_item, data["lang"], "name", rawcontent2, type_)
                if result is None:
                    result = await loop.run_in_executor(None, search_item, "en", "name", rawcontent2, type_)
                if result is None:
                    await reply(message, l('item_notfound'))
                else:
                    if len(result) > 30:
                        await reply(message, l('too_many_items', str(len(result))))
                        return
                    if len(result) == 1:
                        await reply(message, f"{result[0]['type']['displayValue']}: {result[0]['name']} | {result[0]['id']}\n{result[0]['description']}\n{result[0]['rarity']['displayValue']}\n{result[0]['set']['value']}")
                    else:
                        text = str()
                        for count, item in enumerate(result):
                            text += f"\n{count+1} {item['type']['displayValue']}: {item['name']} | {item['id']}"
                        text += f"\n{l('enter_to_show_info')}"
                        await reply(message, text)
                        client.select[message.author.id] = {"exec": [f"await reply(message, f'''{item['type']['displayValue']}: {item['name']} | {item['id']}\n{item['description']}\n{item['rarity']['displayValue']}\n{item['set']['value']}''')" for item in result]}
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['info']}] [[{commands['info_party']}] / [{commands['info_item']}] / [{commands['id']}] / [{commands['skin']}] / [{commands['bag']}] / [{commands['pickaxe']}] / [{commands['emote']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['pending'].split(','):
        try:
            pendings=[]
            for pending in client.pending_friends.values():
                add_cache(client, pending)
                if pending.direction == 'INBOUND':
                    pendings.append(pending)
            if args[1] in commands['true'].split(','):
                for pending in pendings:
                    try:
                        await pending.accept()
                        await reply(message, l('add_friend', f'{str(pending.display_name)} / {pending.id}'))
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                        await reply(message, l('error_while_sending_friendrequest'))
                        continue
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                        await reply(message, l('error'))
                        continue
            elif args[1] in commands['false'].split(','):
                for pending in pendings:
                    try:
                        await pending.decline()
                        await reply(message, l('friend_request_decline', f'{str(pending.display_name)} / {pending.id}'))
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(name,f'>>> {traceback.format_exc()}')
                        await reply(message, l('error_while_declining_friendrequest'))
                        continue
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                        await reply(message, l('error'))
                        continue
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['pending']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['removepending'].split(','):
        try:
            pendings=[]
            for pending in client.pending_friends.values():
                add_cache(client, pending)
                if pending.direction == 'OUTBOUND':
                    pendings.append(pending)
            for pending in pendings:
                try:
                    await pending.decline()
                    await reply(message, l('remove_pending', f'{str(pending.display_name)} / {pending.id}'))
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l('error_while_removing_friendrequest'))
                    continue
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l('error'))
                    continue
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['addfriend'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['addfriend']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is False}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.has_friend(user.id) is False:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.has_friend(user.id) is True:
                    await reply(message, l('already_friend'))
                    return
                await client.add_friend(user.id)
                await reply(message, l('friend_request_to', f'{str(user.display_name)} / {user.id}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.has_friend(user.id) is True:
                await reply(message, l('already_friend'))
                return
            await client.add_friend(user.id)
            await reply(message, l('friend_request_to', f'{str(user.display_name)} / {user.id}'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_sending_friendrequest'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_send_friendrequest')}"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_sending_friendrequest'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['removefriend'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['removefriend']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.has_friend(user.id) is True:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.has_friend(user.id) is False:
                    await reply(message, l('not_friend_with_user'))
                    return
                await client.remove_or_decline_friend(user.id)
                await reply(message, l('remove_friend', f'{str(user.display_name)} / {user.id}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.has_friend(user.id) is False:
                await reply(message, l('not_friend_with_user'))
                return
            await client.remove_or_decline_friend(user.id)
            await reply(message, l('remove_friend', f'{str(user.display_name)} / {user.id}'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_removing_friend')""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_remove_friend')}"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_removing_friend'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['acceptpending'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['acceptpending']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.is_pending(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.is_pending(user.id) is True:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.is_pending(user.id) is False:
                    await reply(message, l('not_pending_with_user'))
                    return
                await client.accept_friend(user.id)
                await reply(message, l('friend_add', f'{str(user.display_name)} / {user.id}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.is_pending(user.id) is False:
                await reply(message, l('not_pending_with_user'))
                return
            await client.accept_friend(user.id)
            await reply(message, l('friend_add', f'{str(user.display_name)} / {user.id}'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_accepting_friendrequest'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_accept_pending')}"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_accepting_friendrequest'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['declinepending'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['declinepending']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.is_pending(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.is_pending(user.id) is True:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.is_pending(user.id) is False:
                    await reply(message, l('nor_pending_with_user'))
                    return
                await client.remove_or_decline_friend(user.id)
                await reply(message, l('friend_request_decline', f'{str(user.display_name)} / {user.id}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.is_pending(user.id) is False:
                await reply(message, l('nor_pending_with_user'))
                return
            await client.remove_or_decline_friend(user.id)
            await reply(message, l('friend_request_decline', f'{str(user.display_name)} / {user.id}'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_declining_friendrequest'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_decline_pending')}"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_declining_friendrequest'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['blockfriend'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['blockfriend']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.is_blocked(user.id) is False}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.is_blocked(user.id) is False:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.is_blocked(user.id) is True:
                    await reply(message, l('already_block'))
                    return
                await client.block_user(user.id)
                await reply(message, l('block_user', f'{str(user.display_name)} / {user.id}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.is_blocked(user.id) is True:
                await reply(message, l('already_block'))
                return
            await client.block_user(user.id)
            await reply(message, l('block_user', f'{str(user.display_name)} / {user.id}'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_blocking_user'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_block_user')}"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_blocking_user'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['unblockfriend'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['unblockfriend']}] [{l('name_or_id')}]")
                return
            users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.is_blocked(user.id) is True}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.is_blocked(user.id) is True:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.is_blocked(user.id) is False:
                    await reply(message, l('not_block'))
                    return
                await client.unblock_user(user.id)
                await reply(message, l('unblock_user', f'{str(user.display_name)} / {user.id}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.is_blocked(user.id) is False:
                await reply(message, l('not_block'))
                return
            await client.unblock_user(user.id)
            await reply(message, l('unblock_user', f'{str(user.display_name)} / {user.id}'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_unblocking_user'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_unblock_user')}"
                await reply(message, text)
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_unblocking_user'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['chatban'].split(','):
        try:
            reason=rawcontent.split(' : ')
            if rawcontent == '':
                await reply(message, f"[{commands['chatban']}] [{l('name_or_id')}] : [{l('reason')}({l('optional')})]")
                return
            users = {str(member.display_name): member for member in client.party.members.values() if rawcontent in str(member.display_name)}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.party.members.get(user.id) is not None:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.party.members.get(user.id) is None:
                    await reply(message, l('user_not_in_party'))
                    return
                member=client.party.members.get(user.id)
                try:
                    await member.chatban(reason[1])
                except IndexError:
                    await member.chatban()
                await reply(message, l('chatban_user', f'{str(user.display_name)} / {user.id}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.party.members.get(user.id) is None:
                await reply(message, l('user_not_in_party'))
                return
            member=client.party.members.get(user.id)
            try:
                await member.chatban(reason[1])
            except IndexError:
                await member.chatban()
            await reply(message, l('chatban_user', f'{str(user.display_name)} / {user.id}'))
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('nor_party_leader'))
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('user_notfound'))
        except ValueError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('already_chatban'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user, "reason": reason} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_chatban')}"
                await reply(message, text)
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('nor_party_leader'))
        except fortnitepy.NotFound:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('user_notfound'))
        except ValueError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('already_chatban'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['promote'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['promote']}] [{l('name_or_id')}]")
                return
            users = {str(member.display_name): member for member in client.party.members.values() if rawcontent in str(member.display_name)}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.party.members.get(user.id) is not None:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.party.members.get(user.id) is None:
                    await reply(message, l('user_not_in_party'))
                    return
                member=client.party.members.get(user.id)
                await member.promote()
                await reply(message, l('promote_user', f'{str(user.display_name)} / {user.id}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.party.members.get(user.id) is None:
                await reply(message, l('user_not_in_party'))
                return
            member=client.party.members.get(user.id)
            await member.promote()
            await reply(message, l('promote_user', f'{str(user.display_name)} / {user.id}'))
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('not_party_leader'))
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('already_party_leader'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_promoting_party_leader'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_promote_user')}"
                await reply(message, text)
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('not_party_leader'))
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('already_party_leader'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_promoting_party_leader'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['kick'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['kick']}] [{l('name_or_id')}]")
                return
            users = {str(member.display_name): member for member in client.party.members.values() if rawcontent in str(member.display_name)}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.party.members.get(user.id) is not None:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.party.members.get(user.id) is None:
                    await reply(message, l('user_not_in_party'))
                    return
                member=client.party.members.get(user.id)
                await member.kick()
                await reply(message, l('kick_user', f'{str(user.display_name)} / {user.id}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.party.members.get(user.id) is None:
                await reply(message, l('user_not_in_party'))
                return
            member=client.party.members.get(user.id)
            await member.kick()
            await reply(message, l('kick_user', f'{str(user.display_name)} / {user.id}'))
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('not_party_leader'))
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('cant_kick_yourself'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_kicking_user'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += "\n数字を入力することでそのユーザーをキックします"
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('not_party_leader'))
        except fortnitepy.PartyError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('cant_kick_yourself'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_kicking_user'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['ready'].split(','):
        try:
            await client.party.me.set_ready(fortnitepy.ReadyState.READY)
            await reply(message, l('set_to', l('readystate'), l('ready')))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['unready'].split(','):
        try:
            await client.party.me.set_ready(fortnitepy.ReadyState.NOT_READY)
            await reply(message, l('set_to', l('readystate'), l('unready')))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['sitout'].split(','):
        try:
            await client.party.me.set_ready(fortnitepy.ReadyState.SITTING_OUT)
            await reply(message, l('set_to', l('readystate'), l('sitout')))
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['match'].split(','):
        try:
            await client.party.me.set_in_match(players_left=int(args[1]) if args[1:2] else 100)
            await reply(message, l('set_to', l('matchstate'), l('remaining', args[1] if args[1:2] else "100")))
        except ValueError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('remaining_must_be_between_0_and_255'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['unmatch'].split(','):
        try:
            await client.party.me.clear_in_match()
            await reply(message, l('set_to', l('matchstate'), l('off')))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['swap'].split(','):
        try:
            if rawcontent == '':
                await reply(message, f"[{commands['kick']}] [{l('name_or_id')}]")
                return
            users = {str(member.display_name): member for member in client.party.members.values() if rawcontent in str(member.display_name)}
            try:
                user=await client.fetch_profile(rawcontent)
                if user is not None:
                    if client.party.members.get(user.id) is not None:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            if len(users) > 30:
                await reply(message, l('too_many_users', str(len(users))))
                return
            if len(users) == 0:
                await reply(message, l('user_notfound'))
                return
            if len(users) == 1:
                user=tuple(users.values())[0]
                if client.party.members.get(user.id) is None:
                    await reply(message, l('user_not_in_party'))
                    return
                member=client.party.members.get(user.id)
                await member.swap_position()
                await reply(message, l('swap_user', f'{str(user.display_name)} / {user.id}'))
            else:
                client.select[message.author.id] = {
                    "exec": [
                        """\
        try:
            if client.party.members.get(user.id) is None:
                await reply(message, l('user_not_in_party'))
                return
            member=client.party.members.get(user.id)
            await member.swap_position()
            await reply(message, l('swap_user', f'{str(user.display_name)} / {user.id}'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_swapping_user'))""" for user in users.values()
                    ],
                    "variable": [
                        {"user": user} for user in users.values()
                    ]
                }
                text = str()
                for count, user in enumerate(users.values()):
                    text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                text += f"\n{l('enter_to_swap_user')}"
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_swapping_user'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['outfitlock'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.outfitlock=True
                await reply(message, l('set_to', l('lock', l('outfit')), l('on')))
            elif args[1] in commands['false'].split(','):
                client.outfitlock=False
                await reply(message, l('set_to', l('lock', l('outfit')), l('off')))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['outfitlock']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['backpacklock'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.backpacklock=True
                await reply(message, l('set_to', l('lock', l('backpack')), l('on')))
            elif args[1] in commands['false'].split(','):
                client.backpacklock=False
                await reply(message, l('set_to', l('lock', l('backpack')), l('off')))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['backpacklock']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['pickaxelock'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.pickaxelock=True
                await reply(message, l('set_to', l('lock', l('pickaxe')), l('on')))
            elif args[1] in commands['false'].split(','):
                client.pickaxelock=False
                await reply(message, l('set_to', l('lock', l('pickaxe')), l('off')))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['pickaxelock']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['emotelock'].split(','):
        try:
            if args[1] in commands['true'].split(','):
                client.emotelock=True
                await reply(message, l('set_to', l('lock', l('emote')), l('on')))
            elif args[1] in commands['false'].split(','):
                client.emotelock=False
                await reply(message, l('set_to', l('lock', l('emote')), l('off')))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['outfitlock']}] [[{commands['true']}] / [{commands['false']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['stop'].split(','):
        try:
            client.stopcheck=True
            if await change_asset(client, message.author.id, "emote", "") is True:
                await reply(message, l('stopped'))
            else:
                await reply(message, l('locked'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['alloutfit'].split(','):
        try:
            flag = False
            if client.outfitlock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, l('locked'))
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allskin = json.load(f)
            for item in allskin['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type']['value'] == 'outfit':
                    if 'banner' not in item['id']:
                        await client.party.me.set_outfit(item['id'])
                    else:
                        await client.party.me.set_outfit(item['id'],variants=client.party.me.create_variants(profile_banner='ProfileBanner'))
                    await asyncio.sleep(2)
            else:
                await reply(message, l('all_end', l('outfit')))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['allbackpack'].split(','):
        try:
            flag = False
            if client.backpacklock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, l('locked'))
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allskin = json.load(f)
            for item in allskin['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type']['value'] == 'backpack':
                    if 'banner' not in item['id']:
                        await client.party.me.set_backpack(item['id'])
                    else:
                        await client.party.me.set_backpack(item['id'],variants=client.party.me.create_variants(profile_banner='ProfileBanner'))
                    await asyncio.sleep(2)
            else:
                await reply(message, l('all_end', l('backpack')))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['allpet'].split(','):
        try:
            flag = False
            if client.backpacklock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, l('locked'))
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allskin = json.load(f)
            for item in allskin['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type']['value'] == 'pet':
                    if 'banner' not in item['id']:
                        await client.party.me.set_backpack(item['id'])
                    else:
                        await client.party.me.set_backpack(item['id'],variants=client.party.me.create_variants(profile_banner='ProfileBanner'))
                    await asyncio.sleep(2)
            else:
                await reply(message, l('all_end', l('pet')))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['allpickaxe'].split(','):
        try:
            flag = False
            if client.pickaxelock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, l('locked'))
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allskin = json.load(f)
            for item in allskin['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type']['value'] == 'pickaxe':
                    if 'banner' not in item['id']:
                        await client.party.me.set_pickaxe(item['id'])
                    else:
                        await client.party.me.set_pickaxe(item['id'],variants=client.party.me.create_variants(profile_banner='ProfileBanner'))
                    await asyncio.sleep(2)
            else:
                await reply(message, l('all_end', l('pickaxe')))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['allemote'].split(','):
        try:
            flag = False
            if client.emotelock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, l('locked'))
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allemote = json.load(f)
            for item in allemote['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type']['value'] == 'emote':
                    await client.party.me.set_emote(item['id'])
                    await asyncio.sleep(5)
            else:
                await reply(message, l('all_end', l('emote')))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['allemoji'].split(','):
        try:
            flag = False
            if client.emotelock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, l('locked'))
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allemote = json.load(f)
            for item in allemote['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type']['value'] == 'emoji':
                    await client.party.me.set_emote(item['id'])
                    await asyncio.sleep(5)
            else:
                await reply(message, l('all_end', l('emoji')))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['alltoy'].split(','):
        try:
            flag = False
            if client.emotelock is True:
                flag = lock_check(client, author_id)
            if flag is True:
                await reply(message, l('locked'))
                return
            with open('allen.json', 'r', encoding='utf-8') as f:
                allemote = json.load(f)
            for item in allemote['data']:
                if client.stopcheck is True:
                    client.stopcheck=False
                    break
                if item['type']['value'] == 'toy':
                    await client.party.me.set_emote(item['id'])
                    await asyncio.sleep(5)
            else:
                await reply(message, l('all_end', l('toy')))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['setenlightenment'].split(','):
        try:
            if await change_asset(client, message.author.id, "outfit", client.party.me.outfit, client.party.me.outfit_variants,(args[1],args[2])) is True:
                await reply(message, l('set_to', 'enlightenment', f'{args[1]}, {args[2]}'))
            else:
                await reply(message, l('locked'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_changing_asset'))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['setenlightenment']}] [{l('number')}] [{l('number')}]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif True in [args[0] in commands[key].split(',') for key in ("cid", "bid", "petcarrier", "pickaxe_id", "eid", "emoji_id", "toy_id", "id")]:
        type_ = convert_to_type(args[0])
        if rawcontent == '':
            await reply(message, f"[{commands[type_]}] [ID]")
            return
        try:
            result = await loop.run_in_executor(None, search_item, data["lang"], "id", rawcontent, type_)
            if result is None:
                result = await loop.run_in_executor(None, search_item, "en", "id", rawcontent, type_)
            if result is None:
                await reply(message, l('item_notfound'))
            else:
                if len(result) > 30:
                    await reply(message, l('too_many_items', str(len(result))))
                    return
                if len(result) == 1:
                    if await change_asset(client, message.author.id, result[0]["type"]["value"], result[0]['id']) is True:
                        await reply(message, f"{result[0]['type']['displayValue']}: {result[0]['name']} | {result[0]['id']}")
                    else:
                        await reply(message, l('locked'))
                else:
                    text = str()
                    for count, item in enumerate(result):
                        text += f"\n{count+1} {item['type']['displayValue']}: {item['name']} | {item['id']}"
                    text += f"\n{l('enter_to_change_asset')}"
                    await reply(message, text)
                    client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{item['type']['value']}', '{item['id']}')" for item in result]}
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_changing_asset'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif True in  [args[0] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe", "emote", "emoji", "toy", "item")]:
        type_ = convert_to_type(args[0])
        if rawcontent == '':
            await reply(message, f"[{commands[type_]}] [{l('itemname')}]")
            return
        try:
            result = await loop.run_in_executor(None, search_item, data["lang"], "name", rawcontent, type_)
            if result is None:
                result = await loop.run_in_executor(None, search_item, "en", "name", rawcontent, type_)
            if result is None:
                await reply(message, l('item_notfound'))
            else:
                if len(result) > 30:
                    await reply(message, l('too_many_items', str(len(result))))
                    return
                if len(result) == 1:
                    if await change_asset(client, message.author.id, result[0]["type"]["value"], result[0]['id']) is True:
                        await reply(message, f"{result[0]['type']['displayValue']}: {result[0]['name']} | {result[0]['id']}")
                    else:
                        await reply(message, l('locked'))
                else:
                    text = str()
                    for count, item in enumerate(result):
                        text += f"\n{count+1} {item['type']['displayValue']}: {item['name']} | {item['id']}"
                    text += f"\n{l('enter_to_change_asset')}"
                    await reply(message, text)
                    client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{item['type']['value']}', '{item['id']}')" for item in result]}
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_changing_asset'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['set'].split(','):
        if rawcontent == '':
            await reply(message, f"[{commands['set']}] [{l('setname')}]")
            return
        try:
            result = await loop.run_in_executor(None, search_item, data["lang"], "set", rawcontent)
            if result is None:
                result = await loop.run_in_executor(None, search_item, "en", "set", rawcontent)
            if result is None:
                await reply(message, l('item_notfound'))
            else:
                if len(result) > 30:
                    await reply(message, l('too_many_items', str(len(result))))
                    return
                if len(result) == 1:
                    if await change_asset(client, message.author.id, result[0]["type"]["value"], result[0]['id']) is True:
                        await reply(message, f"{result[0]['type']['displayValue']}: {result[0]['name']} | {result[0]['id']}({result[0]['set']['value']})")
                    else:
                        await reply(message, l('locked'))
                else:
                    text = str()
                    for count, item in enumerate(result):
                        text += f"\n{count+1} {item['type']['displayValue']}: {item['name']} | {item['id']}({result[0]['set']['value']})"
                    text += f"\n{l('enter_to_change_asset')}"
                    await reply(message, text)
                    client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{item['type']['value']}', '{item['id']}')" for item in result]}
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_changing_asset'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['setstyle'].split(','):
        try:
            if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe")]:
                await reply(message, f"[{commands['setstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                return
            type_ = convert_to_type(args[1])
            id_ = member_asset(client.party.me, convert_to_asset(args[1]))
            result = search_style(data["lang"], id_)
            if result is None:
                await reply(message, l('no_stylechange'))
            else:
                text = str()
                for count, item in enumerate(result):
                    text += f"\n{count+1} {item['name']}"
                text += f"\n{l('enter_to_set_style')}"
                await reply(message, text)
                client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{type_}', '{id_}', {variants['variants']})" for variants in result]}
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['setstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['addstyle'].split(','):
        try:
            if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe")]:
                await reply(message, f"[{commands['addstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                return
            type_ = convert_to_type(args[1])
            id_ = member_asset(client.party.me, convert_to_asset(args[1]))
            variants_ = eval(f"client.party.me.{convert_to_asset(args[1])}_variants")
            result = search_style(data["lang"], id_)
            if result is None:
                await reply(message, l('no_stylechange'))
            else:
                text = str()
                for count, item in enumerate(result):
                    text += f"\n{count+1} {item['name']}"
                text += f"\n{l('enter_to_set_style')}"
                await reply(message, text)
                client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{type_}', '{id_}', {variants_} + {variants['variants']})" for variants in result]}
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['addstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['setvariant'].split(','):
        try:
            if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe")]:
                await reply(message, f"[{commands['setvariant']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                return
            variantdict={}
            for count,text in enumerate(args[2:]):
                if count % 2 != 0:
                    continue
                try:
                    variantdict[text]=args[count+3]
                except IndexError:
                    break
            type_ = convert_to_type(args[1])
            id_ = member_asset(client.party.me, convert_to_asset(args[1]))
            variants = client.party.me.create_variants(item='AthenaCharacter',**variantdict)
            print(variants)
            if await change_asset(client, message.author.id, type_, id_, variants, client.party.me.enlightenments) is False:
                await reply(message, l('locked'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_changing_asset'))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['setvariant']}] [ID] [variant] [{l('number')}]")
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0] in commands['addvariant'].split(','):
        try:
            if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe")]:
                await reply(message, f"[{commands['addvariant']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                return
            variantdict={}
            for count,text in enumerate(args[2:]):
                if count % 2 != 0:
                    continue
                try:
                    variantdict[text]=args[count+3]
                except IndexError:
                    break
            type_ = convert_to_type(args[1])
            id_ = member_asset(client.party.me, convert_to_asset(args[1]))
            variants = client.party.me.create_variants(item='AthenaCharacter',**variantdict)
            variants += eval(f"client.party.me.{convert_to_asset(args[1])}_variants")
            if await change_asset(client, message.author.id, type_, id_, variants, client.party.me.enlightenments) is False:
                await reply(message, l('locked'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_changing_asset'))
        except IndexError:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, f"[{commands['addvariant']}] [ID] [variant] [{l('number')}]")
        except Exception:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif True in [args[0] in commands[key].split(',') for key in ("outfitasset", "backpackasset", "pickaxeasset", "emoteasset")]:
        type_ = convert_to_type(args[0])
        try:
            if rawcontent == '':
                await reply(message, f"[{commands[f'{type_}asset']}] [{l('assetpath')}]")
                return
            if await change_asset(client, message.author.id, type_, rawcontent) is False:
                await reply(message, l('locked'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_changing_asset'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif True in [args[0].lower().startswith(id_) for id_ in ("cid_", "bid_", "petcarrier_", "pickaxe_id_", "eid_", "emoji_", "toy_")]:
        try:
            type_ = convert_to_type("_".join(args[0].split('_')[:-1]) + "_")
            if await change_asset(client, message.author.id, type_, args[0]) is False:
                await reply(message, l('locked'))
        except fortnitepy.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error_while_changing_asset'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    elif args[0].lower().startswith('playlist_'):
        try:
            await client.party.set_playlist(args[0])
            await reply(message, l('set_playlist', args[0]))
            data['fortnite']['playlist']=args[0]
        except fortnitepy.Forbidden:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('not_party_leader'))
        except Exception:
            print(red(traceback.format_exc()))
            dstore(name,f'>>> {traceback.format_exc()}')
            await reply(message, l('error'))

    else:
        if ': ' in message.content:
            return
        if args[0].isdigit() and client.select.get(message.author.id) is not None:
            try:
                if int(args[0]) == 0:
                    await reply(message, l('please_enter_valid_number'))
                    return
                exec_ = client.select[message.author.id]["exec"][int(args[0])-1]
                variable=globals()
                variable.update(locals())
                if client.select[message.author.id].get("variable") is not None:
                    variable.update(client.select[message.author.id]["variable"][int(args[0])-1])
                await aexec(exec_, variable)
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('please_enter_valid_number'))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))
        else:
            result = await loop.run_in_executor(None, search_item, data["lang"], "name", content, "item")
            if result is None:
                result = await loop.run_in_executor(None, search_item, "en", "name", content, "item")
            if result is not None:
                if len(result) > 30:
                    await reply(message, l('too_many_items', str(len(result))))
                    return
                if len(result) == 1:
                    if await change_asset(client, message.author.id, result[0]["type"]["value"], result[0]['id']) is True:
                        await reply(message, f"{result[0]['type']['displayValue']}: {result[0]['name']} | {result[0]['id']}")
                    else:
                        await reply(message, l('locked'))
                else:
                    text = str()
                    for count, item in enumerate(result):
                        text += f"\n{count+1} {item['type']['displayValue']}: {item['name']} | {item['id']}"
                    text += f"\n{l('enter_to_change_asset')}"
                    await reply(message, text)
                    client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{item['type']['value']}', '{item['id']}')" for item in result]}

#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================

dclient=discord.Client()
dclient.isready=False
dclient.owner=None
if data['discord']['enabled'] is True:
    @dclient.event
    async def on_ready() -> None:
        global blacklist_
        global whitelist_
        dclient_user = str(dclient.user)
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(green(f"[{now_()}] {l('login')}: {dclient_user}"))
            dstore(dclient_user,f"{l('login')}: {dclient_user}")
        else:
            if data['no-logs'] is False:
                print(green(f"[{now_()}] {l('login')}: {dclient_user} / {dclient.user.id}"))
            dstore(dclient_user,f"{l('login')}: {dclient_user} / {dclient.user.id}")
        dclient.isready = True
        activity = discord.Game(name=data['discord']['status'])
        await dclient.change_presence(activity=activity)

        for blacklistuser in data['discord']['blacklist']:
            user = dclient.get_user(blacklistuser)
            if user is None:
                try:
                    user = await dclient.fetch_user(blacklistuser)
                except discord.NotFound:
                    if data['loglevel'] == "debug":
                        print(red(traceback.format_exc()))
                        dstore(dclient_user,f'>>> {traceback.format_exc()}')
                    user = None
            if user is None:
                print(red(f"[{now_()}] [{dclient_user}] {l('discord_blacklist_user_notfound', blacklistuser)}"))
                dstore(dclient_user,f">>> {l('discord_blacklist_user_notfound', blacklistuser)}")
            else:
                blacklist_.append(user.id)
                if data['loglevel'] == 'debug':
                    print(yellow(f"{user} / {user.id}"))
        if data['loglevel'] == "debug":
            print(yellow(blacklist_))
        for whitelistuser in data['discord']['whitelist']:
            user = dclient.get_user(whitelistuser)
            if user is None:
                try:
                    user = await dclient.fetch_user(whitelistuser)
                except discord.NotFound:
                    if data['loglevel'] == "debug":
                        print(red(traceback.format_exc()))
                        dstore(dclient_user,f'>>> {traceback.format_exc()}')
                    user = None
            if user is None:
                print(red(f"[{now_()}] [{dclient_user}] {l('discord_whitelist_user_notfound', whitelistuser)}"))
                dstore(dclient_user,f">>> {l('discord_whitelist_user_notfound', whitelistuser)}")
            else:
                whitelist_.append(user.id)
                if data['loglevel'] == 'debug':
                    print(yellow(f"{user.display_name} / {user.id}"))
        if data['loglevel'] == "debug":
            print(yellow(whitelist_))

        try:
            dclient.owner=None
            owner=dclient.get_user(data['discord']['owner'])
            if owner is None:
                try:
                    owner=await dclient.fetch_user(data['discord']['owner'])
                except discord.NotFound:
                    if data['loglevel'] == "debug":
                        print(red(traceback.format_exc()))
                        dstore(dclient_user,f'>>> {traceback.format_exc()}')
                    owner = None
            if owner is None:
                print(red(f"[{now_()}] [{dclient_user}] {l('discord_owner_notfound')}"))
                dstore(dclient_user,">>> {l('discord_owner_notfound')}")
            else:
                dclient.owner=owner
                if data['loglevel'] == 'normal':
                    if data['no-logs'] is False:
                        print(green(f"[{now_()}] [{dclient_user}] {l('owner')}: {dclient.owner}"))
                    dstore(dclient_user,f"{l('owner')}: {dclient.owner}")
                else:
                    if data['no-logs'] is False:
                        print(green(f"[{now_()}] [{dclient_user}] {l('owner')}: {dclient.owner} / {dclient.owner.id}"))
                    dstore(dclient_user,f"{l('owner')}: {dclient.owner} / {dclient.owner.id}")
        except discord.HTTPException:
            if data['loglevel'] == 'debug':
                print(red(traceback.format_exc()))
                dstore(dclient_user,f">>> {traceback.format_exc()}")
            print(red(f"[{now_()}] [{dclient_user}] {l('error_while_requesting_userinfo')}"))
            dstore(dclient_user,f">>> {l('error_while_requesting_userinfo')}")
        except Exception:
            print(red(traceback.format_exc()))
            dstore(dclient_user,f">>> {traceback.format_exc()}")

    @dclient.event
    async def on_message(message: discord.Message) -> None:
        global blacklist
        global whitelist
        global blacklist_
        global whitelist_
        global kill
        if data['discord']['enabled'] is True and dclient.isready is False:
            return
        if message.author == dclient.user:
            return
        if message.author.bot is True and data['discord']['ignorebot'] is True:
            return
        for clientname, client in client_name.items():
            if client.isready is False:
                continue
            if message.channel.name == data['discord']['channelname'].format(name=clientname, id=client.user.id).replace(" ","-").lower():
                break
        else:
            return
        if client.isready is False:
            return
        name=client.user.display_name
        author_id = message.author.id
        loop = asyncio.get_event_loop()
        if message.author.id in blacklist_ and data['discord']['blacklist-ignorecommand'] is True:
            return
        if isinstance(message.channel, discord.TextChannel) is False:
            return
        if not dclient.owner is None:
            if client.discord is False:
                if client.discordperfect is True:
                    return
                elif not message.author.id == dclient.owner.id:
                    return
        else:
            if client.discord is False:
                return
        content=message.content
        if data['caseinsensitive'] is True:
            args = jaconv.kata2hira(content.lower()).split()
        else:
            args = content.split()
        rawargs = content.split()
        rawcontent = ' '.join(rawargs[1:])
        rawcontent2 = ' '.join(rawargs[2:])
        if dclient.owner is not None:
            if client.discord is False:
                if client.discordperfect is True:
                    return
                elif message.author.id != dclient.owner.id and message.author.id not in whitelist_:
                    return
        else:
            if client.discord is False:
                if message.author.id not in whitelist_:
                    return
        if data['loglevel'] == 'normal':
            if data['no-logs'] is False:
                print(f'[{now_()}] [{dclient.user}] {message.author} | {content}')
            dstore(message.author,content)
        else:
            if data['no-logs'] is False:
                print(f'[{now_()}] [{dclient.user}] {message.author} / {message.author.id} | {content}')
            dstore(f'{message.author} / {message.author.id}',content)
        
        flag = False
        if isinstance(message, fortnitepy.message.MessageBase) is True:
            if client.owner is not None:
                if data['fortnite']['whitelist-ownercommand'] is True:
                    if client.owner.id != message.author.id and message.author.id not in whitelist:
                        flag = True
                else:
                    if client.owner.id != message.author.id:
                        flag = True
            else:
                if data['fortnite']['whitelist-ownercommand'] is True:
                    if message.author.id not in whitelist:
                        flag = True
                else:
                    flag = True
        else:
            if client.owner is not None:
                if data['discord']['whitelist-ownercommand'] is True:
                    if client.owner.id != message.author.id and message.author.id not in whitelist_:
                        flag = True
                else:
                    if client.owner.id != message.author.id:
                        flag = True
            else:
                if data['discord']['whitelist-ownercommand'] is True:
                    if message.author.id not in whitelist_:
                        flag = True
                else:
                    flag = True
        if flag is True:
            for checks in commands.items():
                if checks[0] in ignore:
                    continue
                if commands['ownercommands'] == '':
                    break
                for command in commands['ownercommands'].split(','):
                    if args[0] in commands[command.lower()].split(','):
                        await reply(message, l("this_command_owneronly"))
                        return

        if args[0] in commands['prev'].split(','):
            if client.prevmessage.get(message.author.id) is None:
                client.prevmessage[message.author.id]='None'
            content=client.prevmessage.get(message.author.id)
            if data['caseinsensitive'] is True:
                args = jaconv.kata2hira(content.lower()).split()
            else:
                args = content.split()
            args = jaconv.kata2hira(content.lower()).split()
            rawargs = content.split()
            rawcontent = ' '.join(rawargs[1:])
            rawcontent2 = ' '.join(rawargs[2:])
        client.prevmessage[message.author.id]=content

        for key,value in replies.items():
            if args[0] in key.split(','):
                try:
                    await reply(message, value)
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l('error'))
                return

        if data['discord']['enabled'] is True and dclient.isready is True:
            if args[0] in commands['addblacklist_discord'].split(','):
                try:
                    if rawcontent == '' or args[1].isdigit() is False:
                        await reply(message, f"[{commands['addblacklist_discord']}] [{l('userid')}]")
                        return
                    user = dclient.get_user(int(args[1]))
                    if user is None:
                        user = await dclient.fetch_user(int(args[1]))
                    if user.id not in blacklist_:
                        blacklist_.append(user.id)
                        data["discord"]["blacklist"].append(user.id)
                        try:
                            with open("config.json", "r", encoding="utf-8") as f:
                                data_ = json.load(f)
                        except json.decoder.JSONDecodeError:
                            with open("config.json", "r", encoding="utf-8-sig") as f:
                                data_ = json.load(f)
                        data_["discord"]["blacklist"] = data["discord"]["blacklist"]
                        with open("config.json", "w", encoding="utf-8") as f:
                            json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                        await reply(message, l('add_to_list', f'{str(user)} / {str(user.id)}', l('discord_blacklist')))
                    else:
                        await reply(message, l('already_list', f'{str(user)} / {user.id}', l('discord_blacklist')))
                except discord.NotFound:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l('user_notfound'))
                except discord.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
                    dstore(name,f'>>> {l("error_while_requesting_userinfo")}')
                    await reply(message, l("error_while_requesting_userinfo"))
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l('error'))

            elif args[0] in commands['removeblacklist_discord'].split(','):
                try:
                    if rawcontent == '' or args[1].isdigit() is False:
                        await reply(message, f"[{commands['removeblacklist_discord']}] [{l('userid')}]")
                        return
                    user = dclient.get_user(int(args[1]))
                    if user is None:
                        user = await dclient.fetch_user(int(args[1]))
                    if user.id in blacklist_:
                        blacklist_.remove(user.id)
                        data["discord"]["blacklist"].remove(user.id)
                        try:
                            with open("config.json", "r", encoding="utf-8") as f:
                                data_ = json.load(f)
                        except json.decoder.JSONDecodeError:
                            with open("config.json", "r", encoding="utf-8-sig") as f:
                                data_ = json.load(f)
                        data_["discord"]["blacklist"] = data["discord"]["blacklist"]
                        with open("config.json", "w", encoding="utf-8") as f:
                            json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                        await reply(message, l('remove_from_list', f'{str(user)} / {user.id}', l('discord_blacklist')))
                    else:
                        await reply(message, l('not_list', f'{str(user)} / {user.id}', l('discord_blacklist')))
                except discord.NotFound:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l('user_notfound'))
                except discord.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
                    dstore(name,f'>>> {l("error_while_requesting_userinfo")}')
                    await reply(message, l("error_while_requesting_userinfo"))
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l('error'))

            elif args[0] in commands['addwhitelist_discord'].split(','):
                try:
                    if rawcontent == '' or args[1].isdigit() is False:
                        await reply(message, f"[{commands['addwhitelist_discord']}] [{l('userid')}]")
                        return
                    user = dclient.get_user(int(args[1]))
                    if user is None:
                        user = await dclient.fetch_user(int(args[1]))
                    if user.id not in whitelist_:
                        whitelist_.append(user.id)
                        data["discord"]["whitelist"].append(user.id)
                        try:
                            with open("config.json", "r", encoding="utf-8") as f:
                                data_ = json.load(f)
                        except json.decoder.JSONDecodeError:
                            with open("config.json", "r", encoding="utf-8-sig") as f:
                                data_ = json.load(f)
                        data_["discord"]["whitelist"] = data["discord"]["whitelist"]
                        with open("config.json", "w", encoding="utf-8") as f:
                            json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                        await reply(message, l('add_from_list', f'{str(user)} / {user.id}', l('discord_whitelist')))
                    else:
                        await reply(message, l('already_list', f'{str(user)} / {user.id}', l('discord_whitelist')))
                except discord.NotFound:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l('user_notfound'))
                except discord.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
                    dstore(name,f'>>> {l("error_while_requesting_userinfo")}')
                    await reply(message, l("error_while_requesting_userinfo"))
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l('error'))

            elif args[0] in commands['removewhitelist_discord'].split(','):
                try:
                    if rawcontent == '' or args[1].isdigit() is False:
                        await reply(message, f"[{commands['removewhitelist_discord']}] [{l('userid')}]")
                        return
                    user = dclient.get_user(int(args[1]))
                    if user is None:
                        user = await dclient.fetch_user(int(args[1]))
                    if user.id in whitelist_:
                        whitelist_.remove(user.id)
                        data["discord"]["whitelist"].remove(user.id)
                        try:
                            with open("config.json", "r", encoding="utf-8") as f:
                                data_ = json.load(f)
                        except json.decoder.JSONDecodeError:
                            with open("config.json", "r", encoding="utf-8-sig") as f:
                                data_ = json.load(f)
                        data_["discord"]["whitelist"] = data["discord"]["whitelist"]
                        with open("config.json", "w", encoding="utf-8") as f:
                            json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                        await reply(message, l('remove_list', f'{str(user)} / {user.id}', l('discord_whitelist')))
                    else:
                        await reply(message, l('not_list', f'{str(user)} / {user.id}', l('discord_whitelist')))
                except discord.NotFound:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l('user_notfound'))
                except discord.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
                    dstore(name,f'>>> {l("error_while_requesting_userinfo")}')
                    await reply(message, l("error_while_requesting_userinfo"))
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l('error'))

        if args[0] in commands['eval'].split(','):
            try:
                if rawcontent == "":
                    await reply(message, f"[{commands['eval']}] [{l('eval')}]")
                    return
                variable=globals()
                variable.update(locals())
                if rawcontent.startswith("await "):
                    if data['loglevel'] == "debug":
                        print(f"await eval({rawcontent.replace('await ','',1)})")
                    result = await eval(rawcontent.replace("await ","",1), variable)
                    await reply(message, str(result))
                else:
                    if data['loglevel'] == "debug":
                        print(f"eval {rawcontent}")
                    result = eval(rawcontent, variable)
                    await reply(message, str(result))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"{l('error')}\n{traceback.format_exc()}")

        elif args[0] in commands['exec'].split(','):
            try:
                if rawcontent == "":
                    await reply(message, f"[{commands['exec']}] [{l('exec')}]")
                    return
                variable=globals()
                variable.update(locals())
                args_=[i.replace("\\nn", "\n") for i in content.replace("\n", "\\nn").split()]
                content_=" ".join(args_[1:])
                result = await aexec(content_, variable)
                await reply(message, str(result))
            except Exception as e:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"{l('error')}\n{traceback.format_exc()}")

        elif args[0] in commands['restart'].split(','):
            try:
                flag = False
                if client.acceptinvite is False:
                    if isinstance(message, fortnitepy.message.MessageBase) is True:
                        if client.owner is not None:
                            if data['fortnite']['whitelist-ownercommand'] is True:
                                if client.owner.id != message.author.id and message.author.id not in whitelist:
                                    flag = True
                            else:
                                if client.owner.id != message.author.id:
                                    flag = True
                        else:
                            if data['fortnite']['whitelist-ownercommand'] is True:
                                if message.author.id not in whitelist:
                                    flag = True
                            else:
                                flag = True
                    elif isinstance(message, discord.Message) is True:
                        if dclient.owner is not None:
                            if data['discord']['whitelist-ownercommand'] is True:
                                if dclient.owner.id != message.author.id and message.author.id not in whitelist_:
                                    flag = True
                            else:
                                if dclient.owner.id != message.author.id:
                                    flag = True
                        else:
                            if data['discord']['whitelist-ownercommand'] is True:
                                if message.author.id not in whitelist_:
                                    flag = True
                            else:
                                flag = True
                if flag is True:
                    await reply(message, l('invite_is_decline'))
                    return
                await reply(message, l('restaring'))
                os.chdir(os.getcwd())
                os.execv(os.sys.executable,['python', *sys.argv])
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['relogin'].split(','):
            try:
                flag = False
                if client.acceptinvite is False:
                    if isinstance(message, fortnitepy.message.MessageBase) is True:
                        if client.owner is not None:
                            if data['fortnite']['whitelist-ownercommand'] is True:
                                if client.owner.id != message.author.id and message.author.id not in whitelist:
                                    flag = True
                            else:
                                if client.owner.id != message.author.id:
                                    flag = True
                        else:
                            if data['fortnite']['whitelist-ownercommand'] is True:
                                if message.author.id not in whitelist:
                                    flag = True
                            else:
                                flag = True
                    elif isinstance(message, discord.Message) is True:
                        if dclient.owner is not None:
                            if data['discord']['whitelist-ownercommand'] is True:
                                if dclient.owner.id != message.author.id and message.author.id not in whitelist_:
                                    flag = True
                            else:
                                if dclient.owner.id != message.author.id:
                                    flag = True
                        else:
                            if data['discord']['whitelist-ownercommand'] is True:
                                if message.author.id not in whitelist_:
                                    flag = True
                            else:
                                flag = True
                if flag is True:
                    await reply(message, l('invite_is_decline'))
                    return
                await reply(message, l('relogining'))
                await client.restart()
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['reload'].split(','):
            success=reload_configs(client)
            try:
                if success:
                    await reply(message, l('success'))
                else:
                    await reply(message, l('error'))
                    return
                try:
                    client.owner=None
                    owner=await client.fetch_profile(data['fortnite']['owner'])
                    if owner is None:
                        print(red(f'[{now_()}] [{client.user.display_name}] {l("owner_notfound")}'))
                        dstore(client.user.display_name,f'>>> {l("owner_notfound")}')
                    else:
                        add_cache(client, owner)
                        client.owner=client.get_friend(owner.id)
                        if client.owner is None:
                            if data['fortnite']['addfriend'] is True:
                                try:
                                    await client.add_friend(owner.id)
                                except fortnitepy.HTTPException:
                                    if data['loglevel'] == 'debug':
                                        print(red(traceback.format_exc()))
                                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                                    if data['loglevel'] == 'normal':
                                        print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_sending_friendrequest")}'))
                                        dstore(client.user.display_name,f'>>> {l("error_while_sending_friendrequest")}')
                                    else:
                                        print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_sending_friendrequest")}'))
                                    dstore(client.user.display_name,f'>>> {l("error_while_sending_friendrequest")}')
                                except Exception:
                                    print(red(traceback.format_exc()))
                                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                            print(red(f'[{now_()}] [{client.user.display_name}] {l("not_friend_with_owner", commands["reload"])}'))
                            dstore(client.user.display_name,f'>>> {l("not_friend_with_owner", commands["reload"])}')
                        else:
                            if data['loglevel'] == 'normal':
                                if data['no-logs'] is False:
                                    print(green(f'[{now_()}] [{client.user.display_name}] {l("owner")}: {str(client.owner.display_name)}'))
                                dstore(client.user.display_name,f'{l("owner")}: {str(client.owner.display_name)}')
                            else:
                                if data['no-logs'] is False:
                                    print(green(f'[{now_()}] [{client.user.display_name}] {l("owner")}: {str(client.owner.display_name)} / {client.owner.id}'))
                                dstore(client.user.display_name,f'{l("owner")}: {str(client.owner.display_name)} / {client.owner.id}')
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                    print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
                    dstore(client.user.display_name,f'>>> {l("error_while_requesting_userinfo")}')
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(client.user.display_name,f'>>> {traceback.format_exc()}')

                for blacklistuser in data['fortnite']['blacklist']:
                    try:
                        user = await client.fetch_profile(blacklistuser)
                        add_cache(client, user)
                        if user is None:
                            print(red(f'[{now_()}] [{client.user.display_name}] {l("blacklist_user_notfound", blacklistuser)}'))
                            dstore(client.user.display_name,f'>>> {l("blacklist_user_notfound", blacklistuser)}')
                        else:
                            blacklist.append(user.id)
                            if data['loglevel'] == 'debug':
                                print(yellow(f"{str(user.display_name)} / {user.id}"))
                            if data['fortnite']['blacklist-autoblock'] is True:
                                try:
                                    await user.block()
                                except Exception:
                                    if data['loglevel'] == 'debug':
                                        print(red(traceback.format_exc()))
                                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                        print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
                        dstore(client.user.display_name,f'>>> {l("error_while_requesting_userinfo")}')
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                if data['loglevel'] == "debug":
                    print(yellow(blacklist))
                for whitelistuser in data['fortnite']['whitelist']:
                    try:
                        user = await client.fetch_profile(whitelistuser)
                        add_cache(client, user)
                        if user is None:
                            print(red(f'[{now_()}] [{client.user.display_name}] {l("whitelist_user_notfound", whitelistuser)}'))
                            dstore(client.user.display_name,f'>>> {l("whitelist_user_notfound", whitelistuser)}')
                        else:
                            whitelist.append(user.id)
                            if data['loglevel'] == 'debug':
                                print(yellow(f"{str(user.display_name)} / {user.id}"))
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                        print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
                        dstore(client.user.display_name,f'>>> {l("error_while_requesting_userinfo")}')
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                if data['loglevel'] == "debug":
                    print(yellow(whitelist))

                for invitelistuser in data['fortnite']['invitelist']:
                    try:
                        user = await client.fetch_profile(invitelistuser)
                        if user is None:
                            print(red(f'[{now_()}] [{client.user.display_name}] {l("invitelist_user_notfound", invitelistuser)}'))
                            dstore(client.user.display_name,f'>>> {l("invitelist_user_notfound", invitelistuser)}')
                        else:
                            friend = client.get_friend(user.id)
                            if friend is None and user.id != client.user.id:
                                if data['fortnite']['addfriend'] is True:
                                    try:
                                        await client.add_friend(friend.id)
                                    except fortnitepy.HTTPException:
                                        if data['loglevel'] == 'debug':
                                            print(red(traceback.format_exc()))
                                            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                                        if data['loglevel'] == 'normal':
                                            print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_sending_friendrequest")}'))
                                            dstore(client.user.display_name,f'>>> {l("error_while_sending_friendrequest")}')
                                        else:
                                            print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_sending_friendrequest")}'))
                                            dstore(client.user.display_name,f'>>> {l("error_while_sending_friendrequest")}')
                                    except Exception:
                                        print(red(traceback.format_exc()))
                                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                                print(red(f'[{now_()}] [{client.user.display_name}] {l("not_friend_with_inviteuser", invitelistuser)}'))
                                dstore(client.user.display_name,f'>>> {l("not_friend_with_inviteuser", invitelistuser)}')
                            else:
                                add_cache(client, user)
                                client.invitelist.append(user.id)
                                if data['loglevel'] == 'debug':
                                    print(yellow(f"{str(user.display_name)} / {user.id}"))
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                        print(red(f'[{now_()}] [{client.user.display_name}] {l("error_while_requesting_userinfo")}'))
                        dstore(client.user.display_name,f'>>> {l("error_while_requesting_userinfo")}')
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
                if data['loglevel'] == "debug":
                    print(yellow(client.invitelist))
                if data['discord']['enabled'] is True:
                    dclient_user = str(dclient.user)
                    activity = discord.Game(name=data['discord']['status'])
                    await dclient.change_presence(activity=activity)

                    for blacklistuser in data['discord']['blacklist']:
                        user = dclient.get_user(blacklistuser)
                        if user is None:
                            try:
                                user = await dclient.fetch_user(blacklistuser)
                            except discord.NotFound:
                                if data['loglevel'] == "debug":
                                    print(red(traceback.format_exc()))
                                    dstore(dclient_user,f'>>> {traceback.format_exc()}')
                                user = None
                        if user is None:
                            print(red(f'[{now_()}] [{dclient_user}] {l("discord_blacklist_user_notfound", blacklistuser)}'))
                            dstore(dclient_user,f'>>> {l("discord_blacklist_user_notfound", blacklistuser)}')
                        else:
                            blacklist_.append(user.id)
                            if data['loglevel'] == 'debug':
                                print(yellow(f"{user} / {user.id}"))
                    if data['loglevel'] == "debug":
                        print(yellow(blacklist_))
                    for whitelistuser in data['discord']['whitelist']:
                        user = dclient.get_user(whitelistuser)
                        if user is None:
                            try:
                                user = await dclient.fetch_user(whitelistuser)
                            except discord.NotFound:
                                if data['loglevel'] == "debug":
                                    print(red(traceback.format_exc()))
                                    dstore(dclient_user,f'>>> {traceback.format_exc()}')
                                user = None
                        if user is None:
                            print(red(f'[{now_()}] [{dclient_user}] {l("discord_whitelist_user_notfound", whitelistuser)}'))
                            dstore(dclient_user,f'>>> {l("discord_whitelist_user_notfound", whitelistuser)}')
                        else:
                            whitelist_.append(user.id)
                            if data['loglevel'] == 'debug':
                                print(yellow(f"{user.display_name} / {user.id}"))
                    if data['loglevel'] == "debug":
                        print(yellow(whitelist_))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['addblacklist'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['addblacklist']}] [{l('name_or_id')}]")
                    return
                users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(name) and user.id != client.user.id and user.id not in blacklist}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.id not in blacklist:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, l('too_many_users', str(len(users))))
                    return
                if len(users) == 0:
                    await reply(message, l('user_notfound'))
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if user.id not in blacklist:
                        blacklist.append(user.id)
                        if user.display_name is not None:
                            data["fortnite"]["blacklist"].append(str(user.display_name))
                        else:
                            data["fortnite"]["blacklist"].append(user.id)
                        try:
                            with open("config.json", "r", encoding="utf-8") as f:
                                data_ = json.load(f)
                        except json.decoder.JSONDecodeError:
                            with open("config.json", "r", encoding="utf-8-sig") as f:
                                data_ = json.load(f)
                        data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
                        with open("config.json", "w", encoding="utf-8") as f:
                            json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                        await reply(message, l('add_to_list', f'{str(user.display_name)} / {user.id}', l('blacklist')))
                    else:
                        await reply(message, l('already_in_list', f'{str(user.display_name)} / {user.id}', l('blacklist')))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
                if user.id not in blacklist:
                    blacklist.append(user.id)
                    if user.display_name is not None:
                        data["fortnite"]["blacklist"].append(str(user.display_name))
                    else:
                        data["fortnite"]["blacklist"].append(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, l('add_to_list', f'{str(user.display_name)} / {user.id}', l('blacklist')))
                else:
                    await reply(message, l('already_in_list', f'{str(user.display_name)} / {user.id}', l('blacklist')))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                    text += f"\n{l('enter_to_add_to_list', l('blacklist'))}"
                    await reply(message, text)
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['removeblacklist'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['removeblacklist']}] [{l('name_or_id')}]")
                    return
                users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and user.id in blacklist}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.id in blacklist:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, l('too_many_users', str(len(users))))
                    return
                if len(users) == 0:
                    await reply(message, l('user_notfound'))
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if user.id in blacklist:
                        blacklist.remove(user.id)
                        try:
                            data["fortnite"]["blacklist"].remove(str(user.display_name))
                        except ValueError:
                            data["fortnite"]["blacklist"].remove(user.id)
                        try:
                            with open("config.json", "r", encoding="utf-8") as f:
                                data_ = json.load(f)
                        except json.decoder.JSONDecodeError:
                            with open("config.json", "r", encoding="utf-8-sig") as f:
                                data_ = json.load(f)
                        data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
                        with open("config.json", "w", encoding="utf-8") as f:
                            json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                        await reply(message, l('remove_from_list', f'{str(user.display_name)} / {user.id}', l('blacklist')))
                    else:
                        await reply(message, l('not_list', f'{str(user.display_name)} / {user.id}', l('blacklist')))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            if user.id in blacklist:
                blacklist.remove(user.id)
                try:
                    data["fortnite"]["blacklist"].remove(str(user.display_name))
                except ValueError:
                    data["fortnite"]["blacklist"].remove(user.id)
                try:
                    with open("config.json", "r", encoding="utf-8") as f:
                        data_ = json.load(f)
                except json.decoder.JSONDecodeError:
                    with open("config.json", "r", encoding="utf-8-sig") as f:
                        data_ = json.load(f)
                data_["fortnite"]["blacklist"] = data["fortnite"]["blacklist"]
                with open("config.json", "w", encoding="utf-8") as f:
                    json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                await reply(message, l('remove_from_list', f'{str(user.display_name)} / {user.id}', l('blacklist')))
            else:
                await reply(message, l('not_list', f'{str(user.display_name)} / {user.id}', l('blacklist')))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                    text += f"\n{l('enter_to_remove_from_list', l('blacklist'))}"
                    await reply(message, text)
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['addwhitelist'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['addwhitelist']}] [{l('name_or_id')}]")
                    return
                users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and user.id not in whitelist}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.id not in whitelist:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, l('too_many_users', str(len(users))))
                    return
                if len(users) == 0:
                    await reply(message, l('user_notfound'))
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if user.id not in whitelist:
                        whitelist.append(user.id)
                        if user.display_name is not None:
                            data["fortnite"]["whitelist"].append(str(user.display_name))
                        else:
                            data["fortnite"]["whitelist"].append(user.id)
                        try:
                            with open("config.json", "r", encoding="utf-8") as f:
                                data_ = json.load(f)
                        except json.decoder.JSONDecodeError:
                            with open("config.json", "r", encoding="utf-8-sig") as f:
                                data_ = json.load(f)
                        data_["fortnite"]["whitelist"] = data["fortnite"]["whitelist"]
                        with open("config.json", "w", encoding="utf-8") as f:
                            json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                        await reply(message, l("add_to_list", f"{str(user.display_name)} / {user.id}", l('whitelist')))
                    else:
                        await reply(message, l("already_list", f"{str(user.display_name)} / {user.id}", l('whitelist')))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
                if user.id not in whitelist:
                    whitelist.append(user.id)
                    if user.display_name is not None:
                        data["fortnite"]["whitelist"].append(str(user.display_name))
                    else:
                        data["fortnite"]["whitelist"].append(user.id)
                    try:
                        with open("config.json", "r", encoding="utf-8") as f:
                            data_ = json.load(f)
                    except json.decoder.JSONDecodeError:
                        with open("config.json", "r", encoding="utf-8-sig") as f:
                            data_ = json.load(f)
                    data_["fortnite"]["whitelist"] = data["fortnite"]["whitelist"]
                    with open("config.json", "w", encoding="utf-8") as f:
                        json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                    await reply(message, l("add_to_list", f"{str(user.display_name)} / {user.id}", l('whitelist')))
                else:
                    await reply(message, l("already_list", f"{str(user.display_name)} / {user.id}", l('whitelist')))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                    text += f"\n{l('enter_to_add_to_list', l('whitelist'))}"
                    await reply(message, text)
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['removewhitelist'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['removewhitelist']}] [{l('name_or_id')}]")
                    return
                users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and user.id in whitelist}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.id in whitelist:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, l("too_many_users", str(len(users))))
                    return
                if len(users) == 0:
                    await reply(message, l('user_notfound'))
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if user.id in whitelist:
                        whitelist.remove(user.id)
                        try:
                            data["whitelist"].remove(str(user.display_name))
                        except ValueError:
                            data["whitelist"].remove(user.id)
                        try:
                            with open("config.json", "r", encoding="utf-8") as f:
                                data_ = json.load(f)
                        except json.decoder.JSONDecodeError:
                            with open("config.json", "r", encoding="utf-8-sig") as f:
                                data_ = json.load(f)
                        data_["whitelist"] = data["whitelist"]
                        with open("config.json", "w", encoding="utf-8") as f:
                            json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                        await reply(message, l("remove_from_list", f"{str(user.display_name)} / {user.id}", l('whitelist')))
                    else:
                        await reply(message, l("not_list", f"{str(user.display_name)} / {user.id}", l('whitelist')))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            if user.id in whitelist:
                whitelist.remove(user.id)
                try:
                    data["whitelist"].remove(str(user.display_name))
                except ValueError:
                    data["whitelist"].remove(user.id)
                try:
                    with open("config.json", "r", encoding="utf-8") as f:
                        data_ = json.load(f)
                except json.decoder.JSONDecodeError:
                    with open("config.json", "r", encoding="utf-8-sig") as f:
                        data_ = json.load(f)
                data_["whitelist"] = data["whitelist"]
                with open("config.json", "w", encoding="utf-8") as f:
                    json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                await reply(message, l("remove_from_list", f"{str(user.display_name)} / {user.id}", l('whitelist')))
            else:
                await reply(message, l("not_list", f"{str(user.display_name)} / {user.id}", l('whitelist')))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                    text += f"\n{l('enter_to_remove_from_list', l('whitelist'))}"
                    await reply(message, text)
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['addinvitelist'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['addinvitelist']}] [{l('name_or_id')}]")
                    return
                users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and user.id not in client.invitelist}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.id not in client.invitelist:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, l("too_many_users", str(len(users))))
                    return
                if len(users) == 0:
                    await reply(message, l('user_notfound'))
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if user.id not in client.invitelist:
                        client.invitelist.append(user.id)
                        if user.display_name is not None:
                            data["fortnite"]["invitelist"].append(str(user.display_name))
                        else:
                            data["fortnite"]["invitelist"].append(user.id)
                        try:
                            with open("config.json", "r", encoding="utf-8") as f:
                                data_ = json.load(f)
                        except json.decoder.JSONDecodeError:
                            with open("config.json", "r", encoding="utf-8-sig") as f:
                                data_ = json.load(f)
                        data_["fortnite"]["invitelist"] = data["fortnite"]["invitelist"]
                        with open("config.json", "w", encoding="utf-8") as f:
                            json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                        await reply(message, l("add_to_list", f"{str(user.display_name)} / {user.id}", l('invitelist')))
                    else:
                        await reply(message, l("already_list", f"{str(user.display_name)} / {user.id}", l('invitelist')))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            if user.id not in client.invitelist:
                client.invitelist.append(user.id)
                if user.display_name is not None:
                    data["fortnite"]["invitelist"].append(str(user.display_name))
                else:
                    data["fortnite"]["invitelist"].append(user.id)
                try:
                    with open("config.json", "r", encoding="utf-8") as f:
                        data_ = json.load(f)
                except json.decoder.JSONDecodeError:
                    with open("config.json", "r", encoding="utf-8-sig") as f:
                        data_ = json.load(f)
                data_["fortnite"]["invitelist"] = data["fortnite"]["invitelist"]
                with open("config.json", "w", encoding="utf-8") as f:
                    json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                await reply(message, l("add_to_list", f"{str(user.display_name)} / {user.id}", l('invitelist')))
            else:
                await reply(message, l("already_list", f"{str(user.display_name)} / {user.id}", l('invitelist')))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                    text += f"\n{l('enter_to_add_to_list', l('invitelist'))}"
                    await reply(message, text)
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['removeinvitelist'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['removeinvitelist']}] [{l('name_or_id')}]")
                    return
                users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and user.id in client.invitelist}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if user.id in client.invitelist:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, l("too_many_users", str(len(users))))
                    return
                if len(users) == 0:
                    await reply(message, l('user_notfound'))
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if user.id in client.invitelist:
                        client.invitelist.remove(user.id)
                        try:
                            data["fortnite"]["invitelist"].remove(str(user.display_name))
                        except ValueError:
                            data["fortnite"]["invitelist"].remove(user.id)
                        try:
                            with open("config.json", "r", encoding="utf-8") as f:
                                data_ = json.load(f)
                        except json.decoder.JSONDecodeError:
                            with open("config.json", "r", encoding="utf-8-sig") as f:
                                data_ = json.load(f)
                        data_["fortnite"]["invitelist"] = data["fortnite"]["invitelist"]
                        with open("config.json", "w", encoding="utf-8") as f:
                            json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                        await reply(message, l("remove_from_list", f"{str(user.display_name)} / {user.id}", l('invitelist')))
                    else:
                        await reply(message, l("not_list", f"{str(user.display_name)} / {user.id}", l('invitelist')))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            if user.id in client.invitelist:
                client.invitelist.remove(user.id)
                try:
                    data["fortnite"]["invitelist"].remove(str(user.display_name))
                except ValueError:
                    data["fortnite"]["invitelist"].remove(user.id)
                try:
                    with open("config.json", "r", encoding="utf-8") as f:
                        data_ = json.load(f)
                except json.decoder.JSONDecodeError:
                    with open("config.json", "r", encoding="utf-8-sig") as f:
                        data_ = json.load(f)
                data_["fortnite"]["invitelist"] = data["fortnite"]["invitelist"]
                with open("config.json", "w", encoding="utf-8") as f:
                    json.dump(data_, f, ensure_ascii=False, indent=4, sort_keys=False)
                await reply(message, l("remove_from_list", f"{str(user.display_name)} / {user.id}", l('invitelist')))
            else:
                await reply(message, l("not_list", f"{str(user.display_name)} / {user.id}", l('invitelist')))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                    text += f"\n{l('enter_to_remove_from_list', l('invitelist'))}"
                    await reply(message, text)
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['get'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['get']}] [{l('name_or_id')}]")
                    return
                users = {str(member.display_name): member for member in client.party.members.values() if rawcontent in str(member.display_name)}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.party.members.get(user.id) is not None:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, l("too_many_users", str(len(users))))
                    return
                if len(users) == 0:
                    await reply(message, l('user_notfound'))
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    member=client.party.members.get(user.id)
                    if member is None:
                        await reply(message, l("user_not_in_party"))
                        return
                    if data['no-logs'] is False:
                        print(f'{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}')
                    if data['loglevel'] == 'debug':
                        print(json.dumps(member.meta.schema, indent=2))
                    dstore(name,f'{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}')
                    await reply(message, f'{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}')
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            member=client.party.members.get(user.id)
            if member is None:
                await reply(message, l("user_not_in_party"))
                return
            if data['no-logs'] is False:
                print(f'''{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}''')
            if data['loglevel'] == 'debug':
                print(json.dumps(member.meta.schema, indent=2))
            dstore(name,f'''{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}''')
            await reply(message, f'''{str(member.display_name)} / {member.id}\n{member.outfit} {member.outfit_variants}\n{partymember_backpack(member)} {member.backpack_variants}\n{member.pickaxe} {member.pickaxe_variants}\n{partymember_emote(member)}''')""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                    text += f"\n{l('enter_to_get_userinfo')}"
                    await reply(message, text)
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['friendcount'].split(','):
            try:
                if data['no-logs'] is False:
                    print(f"{l('friendcount')}: {len(client.friends)}")
                dstore(name,f"{l('friendcount')}: {len(client.friends)}")
                await reply(message, f"{l('friendcount')}: {len(client.friends)}")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['pendingcount'].split(','):
            try:
                outbound = []
                inbound = []
                for pending in client.pending_friends.values():
                    if pending.direction == 'OUTBOUND':
                        outbound.append(pending)
                    elif pending.direction == 'INBOUND':
                        inbound.append(pending)
                if data['no-logs'] is False:
                    print(f"{l('pendingcount')}: {len(client.pending_friends)}\n{l('outbound')}: {len(outbound)}\n{l('inbound')}: {len(inbound)}")
                dstore(name,f"{l('pendingcount')}: {len(client.pending_friends)}\n{l('outbound')}: {len(outbound)}\n{l('inbound')}: {len(inbound)}")
                await reply(message, f"{l('pendingcount')}: {len(client.pending_friends)}\n{l('outbound')}: {len(outbound)}\n{l('inbound')}: {len(inbound)}")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['blockcount'].split(','):
            try:
                if data['no-logs'] is False:
                    print(f"{l('blockcount')}: {len(client.blocked_users)}")
                dstore(name,f"{l('blockcount')}: {len(client.blocked_users)}")
                await reply(message, f"{l('blockcount')}: {len(client.blocked_users)}")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['friendlist'].split(','):
            try:
                text=''
                for friend in client.friends.values():
                    add_cache(client, friend)
                    text+=f'\n{str(friend.display_name)}'
                if data['no-logs'] is False:
                    print(f'{text}')
                dstore(name,f'{text}')
                await reply(message, f'{text}')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['pendinglist'].split(','):
            try:
                outbound=''
                inbound=''
                for pending in client.pending_friends.values():
                    add_cache(client, pending)
                    if pending.direction == 'OUTBOUND':
                        outbound+=f'\n{str(pending.display_name)}'
                    elif pending.direction == 'INBOUND':
                        inbound+=f'\n{str(pending.display_name)}'
                if data['no-logs'] is False:
                    print(f"{l('outbound')}: {outbound}\n{l('inbound')}: {inbound}")
                dstore(name,f"{l('outbound')}: {outbound}\n{l('inbound')}: {inbound}")
                await reply(message, f"{l('outbound')}: {outbound}\n{l('inbound')}: {inbound}")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['blocklist'].split(','):
            try:
                text=''
                for block in client.blocked_users.values():
                    add_cache(client, block)
                    text+=f'\n{str(block.display_name)}'
                if data['no-logs'] is False:
                    print(f'{text}')
                dstore(name,f'{text}')
                await reply(message, f'{text}')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['outfitmimic'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.outfitmimic=True
                    await reply(message, l('set_to', l('mimic', l('outfit')), l('on')))
                elif args[1] in commands['false'].split(','):
                    client.outfitmimic=False
                    await reply(message, l('set_to', l('mimic', l('outfit')), l('off')))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['skinmimic']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['backpackmimic'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.backpackmimic=True
                    await reply(message, l('mimic_set', l('set_to', l('mimic', l('backpack')), l('on'))))
                elif args[1] in commands['false'].split(','):
                    client.backpackmimic=False
                    await reply(message, l('mimic_set', l('set_to', l('mimic', l('backpack')), l('off'))))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['skinmimic']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['pickaxemimic'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.pickaxemimic=True
                    await reply(message, l('mimic_set', l('set_to', l('mimic', l('pickaxe')), l('on'))))
                elif args[1] in commands['false'].split(','):
                    client.pickaxemimic=False
                    await reply(message, l('mimic_set', l('set_to', l('mimic', l('pickaxe')), l('off'))))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['skinmimic']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['emotemimic'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.emotemimic=True
                    await reply(message, l('mimic_set', l('set_to', l('mimic', l('emote')), l('on'))))
                elif args[1] in commands['false'].split(','):
                    client.emotemimic=False
                    await reply(message, l('mimic_set', l('set_to', l('mimic', l('emote')), l('off'))))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['emotemimic']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['whisper'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.whisper=True
                    await reply(message, l('set_to', l('command_from', l('whisper'), l('on'))))
                elif args[1] in commands['false'].split(','):
                    client.whisper=False
                    await reply(message, l('set_to', l('command_from', l('whisper'), l('off'))))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['whisper']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['partychat'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.partychat=True
                    await reply(message, l('set_to', l('command_from', l('partychat'), l('on'))))
                elif args[1] in commands['false'].split(','):
                    client.partychat=False
                    await reply(message, l('set_to', l('command_from', l('partychat'), l('off'))))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['party']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['discord'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.discord=True
                    await reply(message, l('set_to', l('command_from', l('discord'), l('on'))))
                elif args[1] in commands['false'].split(','):
                    client.discord=False
                    await reply(message, l('set_to', l('command_from', l('discord'), l('off'))))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['discord']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['disablewhisperperfectly'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.whisperperfect=True
                    await reply(message, l('set_to', l('disable_perfect', l('whisper'), l('on'))))
                elif args[1] in commands['false'].split(','):
                    client.whisperperfect=False
                    await reply(message, l('set_to', l('disable_perfect', l('whisper'), l('off'))))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['disablewhisperperfectly']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['disablepartychatperfectly'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.partychatperfect=True
                    await reply(message, l('set_to', l('disable_perfect', l('partychat'), l('on'))))
                elif args[1] in commands['false'].split(','):
                    client.partychatperfect=False
                    await reply(message, l('set_to', l('disable_perfect', l('partychat'), l('on'))))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['disablepartychatperfectly']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['disablediscordperfectly'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.discordperfect=True
                    await reply(message, l('set_to', l('disable_perfect', l('discord'), l('on'))))
                elif args[1] in commands['false'].split(','):
                    client.discordperfect=False
                    await reply(message, l('set_to', l('disable_perfect', l('discord'), l('on'))))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['disablediscordperfectly']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['acceptinvite'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.acceptinvite=True
                    await reply(message, l('set_to', l('invite'), l('accept')))
                elif args[1] in commands['false'].split(','):
                    client.acceptinvite=False
                    await reply(message, l('set_to', l('invite'), l('decline')))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['acceptinvite']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['acceptfriend'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.acceptfriend=True
                    await reply(message, l('set_to', l('friendrequest'), l('accept')))
                elif args[1] in commands['false'].split(','):
                    client.acceptfriend=False
                    await reply(message, l('set_to', l('friendrequest'), l('decline')))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['acceptfriend']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['joinmessageenable'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.joinmessageenable=True
                    await reply(message, l('set_to', l('join_', l('message')), l('on')))
                elif args[1] in commands['false'].split(','):
                    client.joinmessageenable=False
                    await reply(message, l('set_to', l('join_', l('message')), l('off')))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['joinmessageenable']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['randommessageenable'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.randommessageenable=True
                    await reply(message, l('set_to', l('join_', l('randommessage')), l('on')))
                elif args[1] in commands['false'].split(','):
                    client.randommessageenable=False
                    await reply(message, l('set_to', l('join_', l('randommessage')), l('off')))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['randommessageenable']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['wait'].split(','):
            try:
                if client.owner is None:
                    client.acceptinvite=False
                    try:
                        client.timer_.cancel()
                    except AttributeError:
                        pass
                    client.timer_=Timer(data['fortnite']['waitinterval'], inviteaccept, [client])
                    client.timer_.start()
                    await reply(message, l('decline_invite_for', str(data['fortnite']['waitinterval'])))
                else:
                    if client.owner.id in client.party.members.keys() and message.author.id != client.owner.id:
                        await reply(message, l('not_available'))
                        return
                    client.acceptinvite=False
                    try:
                        client.timer_.cancel()
                    except AttributeError:
                        pass
                    client.timer_=Timer(data['fortnite']['waitinterval'], inviteaccept, [client])
                    client.timer_.start()
                    await reply(message, l('decline_invite_for', str(data['fortnite']['waitinterval'])))
            except Exception:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['join'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['join']}] [{l('name_or_id')}]")
                    return
                users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is True}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.has_friend(user.id) is True:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, l('too_many_users', str(len(users))))
                    return
                if len(users) == 0:
                    await reply(message, l('user_notfound'))
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    friend=client.get_friend(user.id)
                    if friend is None:
                        await reply(message, l('not_friend_with_user'))
                    else:
                        await friend.join_party()
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                friend=client.get_friend(user.id)
                if friend is None:
                    await reply(message, l('not_friend_with_user'))
                else:
                    await friend.join_party()
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('party_full_or_already_or_offline'))
            except fortnitepy.NotFound:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('party_notfound'))
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('party_private'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_joining_to_party'))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                    text += f"{l('enter_join_party')}"
                    await reply(message, text)
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('party_full_or_already_or_offline'))
            except fortnitepy.NotFound:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('party_notfound'))
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('party_private'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_joining_to_party'))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['joinid'].split(','):
            try:
                await client.join_to_party(party_id=args[1])
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('party_full_or_already'))
            except fortnitepy.NotFound:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('party_notfound'))
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('party_private'))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['join']}] [{l('party_id')}]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['leave'].split(','):
            try:
                await client.party.me.leave()
                await reply(message, l('party_leave', client.user.party.id))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_leaving_party'))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['invite'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['invite']}] [{l('name_or_id')}]")
                    return
                users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is True}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.has_friend(user.id) is True:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, l('too_many_users', str(len(users))))
                    return
                if len(users) == 0:
                    await reply(message, l('user_notfound'))
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    friend=client.get_friend(user.id)
                    if friend is None:
                        await reply(message, l('not_friend_with_user'))
                        return
                    await friend.invite()
                    await reply(message, l('user_invited', f'{str(friend.display_name)} / {friend.id}', client.party.id))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                friend=client.get_friend(user.id)
                if friend is None:
                    await reply(message, l('not_friend_with_user'))
                    return
                await friend.invite()
                await reply(message, l('user_invited', f'{str(friend.display_name)} / {friend.id}', client.party.id))
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('party_full_or_already'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_sending_partyinvite'))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                    text += f"\n{l('enter_to_invite_user')}"
                    await reply(message, text)
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('party_full_or_already'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_sending_partyinvite'))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['inviteall'].split(','):
            try:
                for inviteuser in client.invitelist:
                    if inviteuser != client.user.id and inviteuser not in client.party.members:
                        try:
                            await client.party.invite(inviteuser)
                        except fortnitepy.PartyError:
                            if data['loglevel'] == 'debug':
                                print(red(traceback.format_exc()))
                                dstore(name,f'>>> {traceback.format_exc()}')
                            await reply(message, l('party_full_or_already'))
                        except fortnitepy.Forbidden:
                            if data['loglevel'] == 'debug':
                                print(red(traceback.format_exc()))
                                dstore(name,f'>>> {traceback.format_exc()}')
                            await reply(message, l('not_friend_with_user'))
                        except fortnitepy.HTTPException:
                            if data['loglevel'] == 'debug':
                                print(red(traceback.format_exc()))
                                dstore(name,f'>>> {traceback.format_exc()}')
                            await reply(message, l('error_while_sending_partyinvite'))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['message'].split(','):
            try:
                send=rawcontent.split(' : ')
                users = {str(user.display_name): user for user in cache_users.values() if send[0] in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is True}
                try:
                    user=await client.fetch_profile(send[0])
                    if user is not None:
                        if client.has_friend(user.id) is True:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, l('too_many_users', str(len(users))))
                    return
                if len(users) == 0:
                    await reply(message, l('user_notfound'))
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    friend=client.get_friend(user.id)
                    if friend is None:
                        await reply(message, l('not_friend_with_user'))
                        return
                    await friend.send(send[1])
                    await reply(message, l('user_sent', f'{str(friend.display_name)} / {friend.id}', send[1]))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                friend=client.get_friend(user.id)
                if friend is None:
                    await reply(message, l('not_friend_with_user'))
                    return
                await friend.send(send[1])
                await reply(message, l('user_sent', f'{str(friend.display_name)} / {friend.id}', send[1]))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user, "send": send} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                    text += f"\n{l('enter_to_send')}"
                    await reply(message, text)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l("error_while_requesting_userinfo"))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['message']}] [{l('name_or_id')}] : [{l('content')}]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['partymessage'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['partymessage']}] [{l('content')}]")
                    return
                await client.party.send(rawcontent)
                await reply(message, l('party_sent', client.party.id, rawcontent))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['status'].split(','):
            try:
                await client.set_status(rawcontent)
                await reply(message, l('set_to', l('status'), rawcontent))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['status']}] [{l('content')}]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['banner'].split(','):
            try:
                await client.party.me.edit_and_keep(partial(client.party.me.set_banner,args[1],args[2],client.party.me.banner[2]))
                await reply(message, l('set_to', l('banner'), f"{args[1]}, {args[2]}"))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_changing_asset'))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['banner']}] [{l('bannerid')}] [{l('color')}]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['level'].split(','):
            try:
                await client.party.me.edit_and_keep(partial(client.party.me.set_banner,client.party.me.banner[0],client.party.me.banner[1],int(args[1])))
                await reply(message, l('level', args[1]))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_changing_asset'))
            except ValueError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('must_be_int'))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['level']}] [{l('level')}]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['bp'].split(','):
            try:
                await client.party.me.edit_and_keep(partial(client.party.me.set_battlepass_info,True,args[1],args[2],args[3]))
                await reply(message, l('set_to', l('bpinfo'), f"{l('tier')}: {args[1]}, {l('xpboost')}: {args[2]}, {l('friendxpboost')}: {args[3]}"))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_changing_bpinfo'))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['bp']}] [{l('tier')}] [{l('xpboost')}] [{l('friendxpboost')}]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['privacy'].split(','):
            try:
                if args[1] in commands['privacy_public'].split(','):
                    await client.party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)
                    await reply(message, l('set_to', l('privacy'), l('public')))
                elif args[1] in commands['privacy_friends_allow_friends_of_friends'].split(','):
                    await client.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS_ALLOW_FRIENDS_OF_FRIENDS)
                    await reply(message, l('set_to', l('privacy'), l('friends_allow_friends_of_friends')))
                elif args[1] in commands['privacy_friends'].split(','):
                    await client.party.set_privacy(fortnitepy.PartyPrivacy.FRIENDS)
                    await reply(message, l('set_to', l('privacy'), l('friends')))
                elif args[1] in commands['privacy_private_allow_friends_of_friends'].split(','):
                    await client.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE_ALLOW_FRIENDS_OF_FRIENDS)
                    await reply(message, l('set_to', l('privacy'), l('private_allow_friends_of_friends')))
                elif args[1] in commands['privacy_private'].split(','):
                    await client.party.set_privacy(fortnitepy.PartyPrivacy.PRIVATE)
                    await reply(message, l('set_to', l('privacy'), l('private')))
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('not_party_leader'))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['privacy']}] [[{commands['privacy_public']}] / [{commands['privacy_friends_allow_friends_of_friends']}] / [{commands['privacy_friends']}] / [{commands['privacy_private_allow_friends_of_friends']}] / [{commands['privacy_private']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error')) 

        elif args[0] in commands['getuser'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['getuser']}] [{l('name_or_id')}]")
                    return
                users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        users[str(user.display_name)] = user
                        add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, l('too_many_users', str(len(users))))
                    return
                if len(users) == 0:
                    await reply(message, l('user_notfound'))
                    return
                text = str()
                for user in users.values():
                    text += f'\n{str(user.display_name)} / {user.id}'
                if data['no-logs'] is False:
                    print(text)
                dstore(name,text)
                await reply(message, text)
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['getfriend'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['getfriend']}] [{l('name_or_id')}]")
                    return
                users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is True}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.has_friend(user.id) is True:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, l('too_many_users', str(len(users))))
                    return
                if len(users) == 0:
                    await reply(message, l('user_notfound'))
                    return
                text = str()
                for user in users.values():
                    friend=client.get_friend(user.id)
                    if friend is None:
                        continue
                    if friend.nickname is None:
                        text += f'\n{str(friend.display_name)} / {friend.id}'
                    else:
                        text += f'\n{friend.nickname}({str(friend.display_name)}) / {friend.id}'
                    if friend.last_logout is not None:
                        text += "\n{1}: {0.year}/{0.month}/{0.day} {0.hour}:{0.minute}:{0.second}".format(friend.last_logout, l('lastlogin'))
                if data['no-logs'] is False:
                    print(text)
                dstore(name,text)
                await reply(message, text)
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['getpending'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['getpending']}] [{l('name_or_id')}]")
                    return
                users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.is_pending(user.id) is True}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.is_pending(user.id) is True:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, l('too_many_users', str(len(users))))
                    return
                if len(users) == 0:
                    await reply(message, l('user_notfound'))
                    return
                text = str()
                for user in users.values():
                    pending = client.get_pending_friend(user.id)
                    if pending is None:
                        continue
                    text += f'\n{str(pending.display_name)} / {pending.id}'
                if data['no-logs'] is False:
                    print(text)
                dstore(name,text)
                await reply(message, text)
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['getblock'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['getblock']}] [{l('name_or_id')}]")
                    return
                users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.is_blocked(user.id) is True}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.is_blocked(user.id) is True:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, l('too_many_users', str(len(users))))
                    return
                if len(users) == 0:
                    await reply(message, l('user_notfound'))
                    return
                text = str()
                for user in users.values():
                    block=client.get_blocked_user(user.id)
                    if block is None:
                        continue
                    text += f'\n{str(block.display_name)} / {block.id}'
                if data['no-logs'] is False:
                    print(text)
                dstore(name,text)
                await reply(message, text)
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['info'].split(','):
            try:
                if args[1] in commands['info_party'].split(','):
                    text = str()
                    text += f"{client.party.id}\n{l('member_count')}: {client.party.member_count}"
                    for member in client.party.members.values():
                        add_cache(client, member)
                        if data['loglevel'] == 'normal':
                            text += f'\n{str(member.display_name)}'
                        else:
                            text += f'\n{str(member.display_name)} / {member.id}'
                    print(text)
                    dstore(None, text)
                    await reply(message, text)
                    if data['loglevel'] == 'debug':
                        print(json.dumps(client.party.meta.schema, indent=2))
                
                elif True in [args[1] in commands[key].split(',') for key in ("cid", "bid", "petcarrier", "pickaxe_id", "eid", "emoji_id", "toy_id", "id")]:
                    type_ = convert_to_type(args[1])
                    if rawcontent2 == '':
                        await reply(message, f"[{commands[type_]}] [ID]")
                        return
                    result = await loop.run_in_executor(None, search_item, data["lang"], "id", rawcontent2, type_)
                    if result is None:
                        result = await loop.run_in_executor(None, search_item, "en", "id", rawcontent2, type_)
                    if result is None:
                        await reply(message, l('item_notfound'))
                    else:
                        if len(result) > 30:
                            await reply(message, l('too_many_items', str(len(result))))
                            return
                        if len(result) == 1:
                            await reply(message, f"{result[0]['type']['displayValue']}: {result[0]['name']} | {result[0]['id']}\n{result[0]['description']}\{result[0]['rarity']['displayValue']}\n{result[0]['set']['value']}")
                        else:
                            text = str()
                            for count, item in enumerate(result):
                                text += f"\n{count+1} {item['type']['displayValue']}: {item['name']} | {item['id']}"
                            text += f"\n{l('enter_to_show_info')}"
                            await reply(message, text)
                            client.select[message.author.id] = {"exec": [f"await reply(message, f'''{item['type']['displayValue']}: {item['name']} | {item['id']}\n{item['description']}\n{item['rarity']['displayValue']}\n{item['set']['value']}''')" for item in result]}

                elif True in  [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe", "emote", "emoji", "toy", "item")]:
                    type_ = convert_to_type(args[1])
                    if rawcontent2 == '':
                        await reply(message, f"[{commands[type_]}] [{l('itemname')}]")
                        return
                    result = await loop.run_in_executor(None, search_item, data["lang"], "name", rawcontent2, type_)
                    if result is None:
                        result = await loop.run_in_executor(None, search_item, "en", "name", rawcontent2, type_)
                    if result is None:
                        await reply(message, l('item_notfound'))
                    else:
                        if len(result) > 30:
                            await reply(message, l('too_many_items', str(len(result))))
                            return
                        if len(result) == 1:
                            await reply(message, f"{result[0]['type']['displayValue']}: {result[0]['name']} | {result[0]['id']}\n{result[0]['description']}\n{result[0]['rarity']['displayValue']}\n{result[0]['set']['value']}")
                        else:
                            text = str()
                            for count, item in enumerate(result):
                                text += f"\n{count+1} {item['type']['displayValue']}: {item['name']} | {item['id']}"
                            text += f"\n{l('enter_to_show_info')}"
                            await reply(message, text)
                            client.select[message.author.id] = {"exec": [f"await reply(message, f'''{item['type']['displayValue']}: {item['name']} | {item['id']}\n{item['description']}\n{item['rarity']['displayValue']}\n{item['set']['value']}''')" for item in result]}
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['info']}] [[{commands['info_party']}] / [{commands['info_item']}] / [{commands['id']}] / [{commands['skin']}] / [{commands['bag']}] / [{commands['pickaxe']}] / [{commands['emote']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['pending'].split(','):
            try:
                pendings=[]
                for pending in client.pending_friends.values():
                    add_cache(client, pending)
                    if pending.direction == 'INBOUND':
                        pendings.append(pending)
                if args[1] in commands['true'].split(','):
                    for pending in pendings:
                        try:
                            await pending.accept()
                            await reply(message, l('add_friend', f'{str(pending.display_name)} / {pending.id}'))
                        except fortnitepy.HTTPException:
                            if data['loglevel'] == 'debug':
                                print(red(traceback.format_exc()))
                            await reply(message, l('error_while_sending_friendrequest'))
                            continue
                        except Exception:
                            print(red(traceback.format_exc()))
                            dstore(name,f'>>> {traceback.format_exc()}')
                            await reply(message, l('error'))
                            continue
                elif args[1] in commands['false'].split(','):
                    for pending in pendings:
                        try:
                            await pending.decline()
                            await reply(message, l('friend_request_decline', f'{str(pending.display_name)} / {pending.id}'))
                        except fortnitepy.HTTPException:
                            if data['loglevel'] == 'debug':
                                print(red(traceback.format_exc()))
                                dstore(name,f'>>> {traceback.format_exc()}')
                            await reply(message, l('error_while_declining_friendrequest'))
                            continue
                        except Exception:
                            print(red(traceback.format_exc()))
                            dstore(name,f'>>> {traceback.format_exc()}')
                            await reply(message, l('error'))
                            continue
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['pending']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['removepending'].split(','):
            try:
                pendings=[]
                for pending in client.pending_friends.values():
                    add_cache(client, pending)
                    if pending.direction == 'OUTBOUND':
                        pendings.append(pending)
                for pending in pendings:
                    try:
                        await pending.decline()
                        await reply(message, l('remove_pending', f'{str(pending.display_name)} / {pending.id}'))
                    except fortnitepy.HTTPException:
                        if data['loglevel'] == 'debug':
                            print(red(traceback.format_exc()))
                            dstore(name,f'>>> {traceback.format_exc()}')
                        await reply(message, l('error_while_removing_friendrequest'))
                        continue
                    except Exception:
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                        await reply(message, l('error'))
                        continue
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['addfriend'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['addfriend']}] [{l('name_or_id')}]")
                    return
                users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is False}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.has_friend(user.id) is False:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, l('too_many_users', str(len(users))))
                    return
                if len(users) == 0:
                    await reply(message, l('user_notfound'))
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.has_friend(user.id) is True:
                        await reply(message, l('already_friend'))
                        return
                    await client.add_friend(user.id)
                    await reply(message, l('friend_request_to', f'{str(user.display_name)} / {user.id}'))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.has_friend(user.id) is True:
                    await reply(message, l('already_friend'))
                    return
                await client.add_friend(user.id)
                await reply(message, l('friend_request_to', f'{str(user.display_name)} / {user.id}'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_sending_friendrequest'))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                    text += f"\n{l('enter_to_send_friendrequest')}"
                    await reply(message, text)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_sending_friendrequest'))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['removefriend'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['removefriend']}] [{l('name_or_id')}]")
                    return
                users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.has_friend(user.id) is True}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.has_friend(user.id) is True:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, l('too_many_users', str(len(users))))
                    return
                if len(users) == 0:
                    await reply(message, l('user_notfound'))
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.has_friend(user.id) is False:
                        await reply(message, l('not_friend_with_user'))
                        return
                    await client.remove_or_decline_friend(user.id)
                    await reply(message, l('remove_friend', f'{str(user.display_name)} / {user.id}'))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.has_friend(user.id) is False:
                    await reply(message, l('not_friend_with_user'))
                    return
                await client.remove_or_decline_friend(user.id)
                await reply(message, l('remove_friend', f'{str(user.display_name)} / {user.id}'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_removing_friend')""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                    text += f"\n{l('enter_to_remove_friend')}"
                    await reply(message, text)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_removing_friend'))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['acceptpending'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['acceptpending']}] [{l('name_or_id')}]")
                    return
                users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.is_pending(user.id) is True}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.is_pending(user.id) is True:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, l('too_many_users', str(len(users))))
                    return
                if len(users) == 0:
                    await reply(message, l('user_notfound'))
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.is_pending(user.id) is False:
                        await reply(message, l('not_pending_with_user'))
                        return
                    await client.accept_friend(user.id)
                    await reply(message, l('friend_add', f'{str(user.display_name)} / {user.id}'))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.is_pending(user.id) is False:
                    await reply(message, l('not_pending_with_user'))
                    return
                await client.accept_friend(user.id)
                await reply(message, l('friend_add', f'{str(user.display_name)} / {user.id}'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_accepting_friendrequest'))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                    text += f"\n{l('enter_to_accept_pending')}"
                    await reply(message, text)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_accepting_friendrequest'))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['declinepending'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['declinepending']}] [{l('name_or_id')}]")
                    return
                users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.is_pending(user.id) is True}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.is_pending(user.id) is True:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, l('too_many_users', str(len(users))))
                    return
                if len(users) == 0:
                    await reply(message, l('user_notfound'))
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.is_pending(user.id) is False:
                        await reply(message, l('nor_pending_with_user'))
                        return
                    await client.remove_or_decline_friend(user.id)
                    await reply(message, l('friend_request_decline', f'{str(user.display_name)} / {user.id}'))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.is_pending(user.id) is False:
                    await reply(message, l('nor_pending_with_user'))
                    return
                await client.remove_or_decline_friend(user.id)
                await reply(message, l('friend_request_decline', f'{str(user.display_name)} / {user.id}'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_declining_friendrequest'))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                    text += f"\n{l('enter_to_decline_pending')}"
                    await reply(message, text)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_declining_friendrequest'))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['blockfriend'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['blockfriend']}] [{l('name_or_id')}]")
                    return
                users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.is_blocked(user.id) is False}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.is_blocked(user.id) is False:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, l('too_many_users', str(len(users))))
                    return
                if len(users) == 0:
                    await reply(message, l('user_notfound'))
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.is_blocked(user.id) is True:
                        await reply(message, l('already_block'))
                        return
                    await client.block_user(user.id)
                    await reply(message, l('block_user', f'{str(user.display_name)} / {user.id}'))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.is_blocked(user.id) is True:
                    await reply(message, l('already_block'))
                    return
                await client.block_user(user.id)
                await reply(message, l('block_user', f'{str(user.display_name)} / {user.id}'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_blocking_user'))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                    text += f"\n{l('enter_to_block_user')}"
                    await reply(message, text)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_blocking_user'))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['unblockfriend'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['unblockfriend']}] [{l('name_or_id')}]")
                    return
                users = {str(user.display_name): user for user in cache_users.values() if rawcontent in str(user.display_name) and user.id != client.user.id and client.is_blocked(user.id) is True}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.is_blocked(user.id) is True:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, l('too_many_users', str(len(users))))
                    return
                if len(users) == 0:
                    await reply(message, l('user_notfound'))
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.is_blocked(user.id) is False:
                        await reply(message, l('not_block'))
                        return
                    await client.unblock_user(user.id)
                    await reply(message, l('unblock_user', f'{str(user.display_name)} / {user.id}'))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.is_blocked(user.id) is False:
                    await reply(message, l('not_block'))
                    return
                await client.unblock_user(user.id)
                await reply(message, l('unblock_user', f'{str(user.display_name)} / {user.id}'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_unblocking_user'))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                    text += f"\n{l('enter_to_unblock_user')}"
                    await reply(message, text)
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_unblocking_user'))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['chatban'].split(','):
            try:
                reason=rawcontent.split(' : ')
                if rawcontent == '':
                    await reply(message, f"[{commands['chatban']}] [{l('name_or_id')}] : [{l('reason')}({l('optional')})]")
                    return
                users = {str(member.display_name): member for member in client.party.members.values() if rawcontent in str(member.display_name)}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.party.members.get(user.id) is not None:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, l('too_many_users', str(len(users))))
                    return
                if len(users) == 0:
                    await reply(message, l('user_notfound'))
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.party.members.get(user.id) is None:
                        await reply(message, l('user_not_in_party'))
                        return
                    member=client.party.members.get(user.id)
                    try:
                        await member.chatban(reason[1])
                    except IndexError:
                        await member.chatban()
                    await reply(message, l('chatban_user', f'{str(user.display_name)} / {user.id}'))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.party.members.get(user.id) is None:
                    await reply(message, l('user_not_in_party'))
                    return
                member=client.party.members.get(user.id)
                try:
                    await member.chatban(reason[1])
                except IndexError:
                    await member.chatban()
                await reply(message, l('chatban_user', f'{str(user.display_name)} / {user.id}'))
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('nor_party_leader'))
            except fortnitepy.NotFound:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('user_notfound'))
            except ValueError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('already_chatban'))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user, "reason": reason} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                    text += f"\n{l('enter_to_chatban')}"
                    await reply(message, text)
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('nor_party_leader'))
            except fortnitepy.NotFound:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('user_notfound'))
            except ValueError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('already_chatban'))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['promote'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['promote']}] [{l('name_or_id')}]")
                    return
                users = {str(member.display_name): member for member in client.party.members.values() if rawcontent in str(member.display_name)}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.party.members.get(user.id) is not None:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, l('too_many_users', str(len(users))))
                    return
                if len(users) == 0:
                    await reply(message, l('user_notfound'))
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.party.members.get(user.id) is None:
                        await reply(message, l('user_not_in_party'))
                        return
                    member=client.party.members.get(user.id)
                    await member.promote()
                    await reply(message, l('promote_user', f'{str(user.display_name)} / {user.id}'))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.party.members.get(user.id) is None:
                    await reply(message, l('user_not_in_party'))
                    return
                member=client.party.members.get(user.id)
                await member.promote()
                await reply(message, l('promote_user', f'{str(user.display_name)} / {user.id}'))
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('not_party_leader'))
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('already_party_leader'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_promoting_party_leader'))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                    text += f"\n{l('enter_to_promote_user')}"
                    await reply(message, text)
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('not_party_leader'))
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('already_party_leader'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_promoting_party_leader'))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['kick'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['kick']}] [{l('name_or_id')}]")
                    return
                users = {str(member.display_name): member for member in client.party.members.values() if rawcontent in str(member.display_name)}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.party.members.get(user.id) is not None:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, l('too_many_users', str(len(users))))
                    return
                if len(users) == 0:
                    await reply(message, l('user_notfound'))
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.party.members.get(user.id) is None:
                        await reply(message, l('user_not_in_party'))
                        return
                    member=client.party.members.get(user.id)
                    await member.kick()
                    await reply(message, l('kick_user', f'{str(user.display_name)} / {user.id}'))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.party.members.get(user.id) is None:
                    await reply(message, l('user_not_in_party'))
                    return
                member=client.party.members.get(user.id)
                await member.kick()
                await reply(message, l('kick_user', f'{str(user.display_name)} / {user.id}'))
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('not_party_leader'))
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('cant_kick_yourself'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_kicking_user'))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                    text += "\n数字を入力することでそのユーザーをキックします"
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('not_party_leader'))
            except fortnitepy.PartyError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('cant_kick_yourself'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_kicking_user'))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['ready'].split(','):
            try:
                await client.party.me.set_ready(fortnitepy.ReadyState.READY)
                await reply(message, l('set_to', l('readystate'), l('ready')))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['unready'].split(','):
            try:
                await client.party.me.set_ready(fortnitepy.ReadyState.NOT_READY)
                await reply(message, l('set_to', l('readystate'), l('unready')))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['sitout'].split(','):
            try:
                await client.party.me.set_ready(fortnitepy.ReadyState.SITTING_OUT)
                await reply(message, l('set_to', l('readystate'), l('sitout')))
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['match'].split(','):
            try:
                await client.party.me.set_in_match(players_left=int(args[1]) if args[1:2] else 100)
                await reply(message, l('set_to', l('matchstate'), l('remaining', args[1] if args[1:2] else "100")))
            except ValueError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('remaining_must_be_between_0_and_255'))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['unmatch'].split(','):
            try:
                await client.party.me.clear_in_match()
                await reply(message, l('set_to', l('matchstate'), l('off')))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['swap'].split(','):
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands['kick']}] [{l('name_or_id')}]")
                    return
                users = {str(member.display_name): member for member in client.party.members.values() if rawcontent in str(member.display_name)}
                try:
                    user=await client.fetch_profile(rawcontent)
                    if user is not None:
                        if client.party.members.get(user.id) is not None:
                            users[str(user.display_name)] = user
                            add_cache(client, user)
                except fortnitepy.HTTPException:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l("error_while_requesting_userinfo"))
                if len(users) > 30:
                    await reply(message, l('too_many_users', str(len(users))))
                    return
                if len(users) == 0:
                    await reply(message, l('user_notfound'))
                    return
                if len(users) == 1:
                    user=tuple(users.values())[0]
                    if client.party.members.get(user.id) is None:
                        await reply(message, l('user_not_in_party'))
                        return
                    member=client.party.members.get(user.id)
                    await member.swap_position()
                    await reply(message, l('swap_user', f'{str(user.display_name)} / {user.id}'))
                else:
                    client.select[message.author.id] = {
                        "exec": [
                            """\
            try:
                if client.party.members.get(user.id) is None:
                    await reply(message, l('user_not_in_party'))
                    return
                member=client.party.members.get(user.id)
                await member.swap_position()
                await reply(message, l('swap_user', f'{str(user.display_name)} / {user.id}'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_swapping_user'))""" for user in users.values()
                        ],
                        "variable": [
                            {"user": user} for user in users.values()
                        ]
                    }
                    text = str()
                    for count, user in enumerate(users.values()):
                        text += f"\n{count+1} {str(user.display_name)} / {user.id}"
                    text += f"\n{l('enter_to_swap_user')}"
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_swapping_user'))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['outfitlock'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.outfitlock=True
                    await reply(message, l('set_to', l('lock', l('outfit')), l('on')))
                elif args[1] in commands['false'].split(','):
                    client.outfitlock=False
                    await reply(message, l('set_to', l('lock', l('outfit')), l('off')))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['outfitlock']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['backpacklock'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.backpacklock=True
                    await reply(message, l('set_to', l('lock', l('backpack')), l('on')))
                elif args[1] in commands['false'].split(','):
                    client.backpacklock=False
                    await reply(message, l('set_to', l('lock', l('backpack')), l('off')))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['backpacklock']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['pickaxelock'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.pickaxelock=True
                    await reply(message, l('set_to', l('lock', l('pickaxe')), l('on')))
                elif args[1] in commands['false'].split(','):
                    client.pickaxelock=False
                    await reply(message, l('set_to', l('lock', l('pickaxe')), l('off')))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['pickaxelock']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['emotelock'].split(','):
            try:
                if args[1] in commands['true'].split(','):
                    client.emotelock=True
                    await reply(message, l('set_to', l('lock', l('emote')), l('on')))
                elif args[1] in commands['false'].split(','):
                    client.emotelock=False
                    await reply(message, l('set_to', l('lock', l('emote')), l('off')))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['outfitlock']}] [[{commands['true']}] / [{commands['false']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['stop'].split(','):
            try:
                client.stopcheck=True
                if await change_asset(client, message.author.id, "emote", "") is True:
                    await reply(message, l('stopped'))
                else:
                    await reply(message, l('locked'))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['alloutfit'].split(','):
            try:
                flag = False
                if client.outfitlock is True:
                    flag = lock_check(client, author_id)
                if flag is True:
                    await reply(message, l('locked'))
                    return
                with open('allen.json', 'r', encoding='utf-8') as f:
                    allskin = json.load(f)
                for item in allskin['data']:
                    if client.stopcheck is True:
                        client.stopcheck=False
                        break
                    if item['type']['value'] == 'outfit':
                        if 'banner' not in item['id']:
                            await client.party.me.set_outfit(item['id'])
                        else:
                            await client.party.me.set_outfit(item['id'],variants=client.party.me.create_variants(profile_banner='ProfileBanner'))
                        await asyncio.sleep(2)
                else:
                    await reply(message, l('all_end', l('outfit')))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['allbackpack'].split(','):
            try:
                flag = False
                if client.backpacklock is True:
                    flag = lock_check(client, author_id)
                if flag is True:
                    await reply(message, l('locked'))
                    return
                with open('allen.json', 'r', encoding='utf-8') as f:
                    allskin = json.load(f)
                for item in allskin['data']:
                    if client.stopcheck is True:
                        client.stopcheck=False
                        break
                    if item['type']['value'] == 'backpack':
                        if 'banner' not in item['id']:
                            await client.party.me.set_backpack(item['id'])
                        else:
                            await client.party.me.set_backpack(item['id'],variants=client.party.me.create_variants(profile_banner='ProfileBanner'))
                        await asyncio.sleep(2)
                else:
                    await reply(message, l('all_end', l('backpack')))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['allpet'].split(','):
            try:
                flag = False
                if client.backpacklock is True:
                    flag = lock_check(client, author_id)
                if flag is True:
                    await reply(message, l('locked'))
                    return
                with open('allen.json', 'r', encoding='utf-8') as f:
                    allskin = json.load(f)
                for item in allskin['data']:
                    if client.stopcheck is True:
                        client.stopcheck=False
                        break
                    if item['type']['value'] == 'pet':
                        if 'banner' not in item['id']:
                            await client.party.me.set_backpack(item['id'])
                        else:
                            await client.party.me.set_backpack(item['id'],variants=client.party.me.create_variants(profile_banner='ProfileBanner'))
                        await asyncio.sleep(2)
                else:
                    await reply(message, l('all_end', l('pet')))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['allpickaxe'].split(','):
            try:
                flag = False
                if client.pickaxelock is True:
                    flag = lock_check(client, author_id)
                if flag is True:
                    await reply(message, l('locked'))
                    return
                with open('allen.json', 'r', encoding='utf-8') as f:
                    allskin = json.load(f)
                for item in allskin['data']:
                    if client.stopcheck is True:
                        client.stopcheck=False
                        break
                    if item['type']['value'] == 'pickaxe':
                        if 'banner' not in item['id']:
                            await client.party.me.set_pickaxe(item['id'])
                        else:
                            await client.party.me.set_pickaxe(item['id'],variants=client.party.me.create_variants(profile_banner='ProfileBanner'))
                        await asyncio.sleep(2)
                else:
                    await reply(message, l('all_end', l('pickaxe')))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['allemote'].split(','):
            try:
                flag = False
                if client.emotelock is True:
                    flag = lock_check(client, author_id)
                if flag is True:
                    await reply(message, l('locked'))
                    return
                with open('allen.json', 'r', encoding='utf-8') as f:
                    allemote = json.load(f)
                for item in allemote['data']:
                    if client.stopcheck is True:
                        client.stopcheck=False
                        break
                    if item['type']['value'] == 'emote':
                        await client.party.me.set_emote(item['id'])
                        await asyncio.sleep(5)
                else:
                    await reply(message, l('all_end', l('emote')))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['allemoji'].split(','):
            try:
                flag = False
                if client.emotelock is True:
                    flag = lock_check(client, author_id)
                if flag is True:
                    await reply(message, l('locked'))
                    return
                with open('allen.json', 'r', encoding='utf-8') as f:
                    allemote = json.load(f)
                for item in allemote['data']:
                    if client.stopcheck is True:
                        client.stopcheck=False
                        break
                    if item['type']['value'] == 'emoji':
                        await client.party.me.set_emote(item['id'])
                        await asyncio.sleep(5)
                else:
                    await reply(message, l('all_end', l('emoji')))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['alltoy'].split(','):
            try:
                flag = False
                if client.emotelock is True:
                    flag = lock_check(client, author_id)
                if flag is True:
                    await reply(message, l('locked'))
                    return
                with open('allen.json', 'r', encoding='utf-8') as f:
                    allemote = json.load(f)
                for item in allemote['data']:
                    if client.stopcheck is True:
                        client.stopcheck=False
                        break
                    if item['type']['value'] == 'toy':
                        await client.party.me.set_emote(item['id'])
                        await asyncio.sleep(5)
                else:
                    await reply(message, l('all_end', l('toy')))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['setenlightenment'].split(','):
            try:
                if await change_asset(client, message.author.id, "outfit", client.party.me.outfit, client.party.me.outfit_variants,(args[1],args[2])) is True:
                    await reply(message, l('set_to', 'enlightenment', f'{args[1]}, {args[2]}'))
                else:
                    await reply(message, l('locked'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_changing_asset'))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['setenlightenment']}] [{l('number')}] [{l('number')}]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif True in [args[0] in commands[key].split(',') for key in ("cid", "bid", "petcarrier", "pickaxe_id", "eid", "emoji_id", "toy_id", "id")]:
            type_ = convert_to_type(args[0])
            if rawcontent == '':
                await reply(message, f"[{commands[type_]}] [ID]")
                return
            try:
                result = await loop.run_in_executor(None, search_item, data["lang"], "id", rawcontent, type_)
                if result is None:
                    result = await loop.run_in_executor(None, search_item, "en", "id", rawcontent, type_)
                if result is None:
                    await reply(message, l('item_notfound'))
                else:
                    if len(result) > 30:
                        await reply(message, l('too_many_items', str(len(result))))
                        return
                    if len(result) == 1:
                        if await change_asset(client, message.author.id, result[0]["type"]["value"], result[0]['id']) is True:
                            await reply(message, f"{result[0]['type']['displayValue']}: {result[0]['name']} | {result[0]['id']}")
                        else:
                            await reply(message, l('locked'))
                    else:
                        text = str()
                        for count, item in enumerate(result):
                            text += f"\n{count+1} {item['type']['displayValue']}: {item['name']} | {item['id']}"
                        text += f"\n{l('enter_to_change_asset')}"
                        await reply(message, text)
                        client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{item['type']['value']}', '{item['id']}')" for item in result]}
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_changing_asset'))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif True in  [args[0] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe", "emote", "emoji", "toy", "item")]:
            type_ = convert_to_type(args[0])
            if rawcontent == '':
                await reply(message, f"[{commands[type_]}] [{l('itemname')}]")
                return
            try:
                result = await loop.run_in_executor(None, search_item, data["lang"], "name", rawcontent, type_)
                if result is None:
                    result = await loop.run_in_executor(None, search_item, "en", "name", rawcontent, type_)
                if result is None:
                    await reply(message, l('item_notfound'))
                else:
                    if len(result) > 30:
                        await reply(message, l('too_many_items', str(len(result))))
                        return
                    if len(result) == 1:
                        if await change_asset(client, message.author.id, result[0]["type"]["value"], result[0]['id']) is True:
                            await reply(message, f"{result[0]['type']['displayValue']}: {result[0]['name']} | {result[0]['id']}")
                        else:
                            await reply(message, l('locked'))
                    else:
                        text = str()
                        for count, item in enumerate(result):
                            text += f"\n{count+1} {item['type']['displayValue']}: {item['name']} | {item['id']}"
                        text += f"\n{l('enter_to_change_asset')}"
                        await reply(message, text)
                        client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{item['type']['value']}', '{item['id']}')" for item in result]}
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_changing_asset'))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['set'].split(','):
            if rawcontent == '':
                await reply(message, f"[{commands['set']}] [{l('setname')}]")
                return
            try:
                result = await loop.run_in_executor(None, search_item, data["lang"], "set", rawcontent)
                if result is None:
                    result = await loop.run_in_executor(None, search_item, "en", "set", rawcontent)
                if result is None:
                    await reply(message, l('item_notfound'))
                else:
                    if len(result) > 30:
                        await reply(message, l('too_many_items', str(len(result))))
                        return
                    if len(result) == 1:
                        if await change_asset(client, message.author.id, result[0]["type"]["value"], result[0]['id']) is True:
                            await reply(message, f"{result[0]['type']['displayValue']}: {result[0]['name']} | {result[0]['id']}({result[0]['set']['value']})")
                        else:
                            await reply(message, l('locked'))
                    else:
                        text = str()
                        for count, item in enumerate(result):
                            text += f"\n{count+1} {item['type']['displayValue']}: {item['name']} | {item['id']}({result[0]['set']['value']})"
                        text += f"\n{l('enter_to_change_asset')}"
                        await reply(message, text)
                        client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{item['type']['value']}', '{item['id']}')" for item in result]}
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_changing_asset'))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['setstyle'].split(','):
            try:
                if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe")]:
                    await reply(message, f"[{commands['setstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                    return
                type_ = convert_to_type(args[1])
                id_ = member_asset(client.party.me, convert_to_asset(args[1]))
                result = search_style(data["lang"], id_)
                if result is None:
                    await reply(message, l('no_stylechange'))
                else:
                    text = str()
                    for count, item in enumerate(result):
                        text += f"\n{count+1} {item['name']}"
                    text += f"\n{l('enter_to_set_style')}"
                    await reply(message, text)
                    client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{type_}', '{id_}', {variants['variants']})" for variants in result]}
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['setstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['addstyle'].split(','):
            try:
                if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe")]:
                    await reply(message, f"[{commands['addstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                    return
                type_ = convert_to_type(args[1])
                id_ = member_asset(client.party.me, convert_to_asset(args[1]))
                variants_ = eval(f"client.party.me.{convert_to_asset(args[1])}_variants")
                result = search_style(data["lang"], id_)
                if result is None:
                    await reply(message, l('no_stylechange'))
                else:
                    text = str()
                    for count, item in enumerate(result):
                        text += f"\n{count+1} {item['name']}"
                    text += f"\n{l('enter_to_set_style')}"
                    await reply(message, text)
                    client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{type_}', '{id_}', {variants_} + {variants['variants']})" for variants in result]}
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['addstyle']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['setvariant'].split(','):
            try:
                if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe")]:
                    await reply(message, f"[{commands['setvariant']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                    return
                variantdict={}
                for count,text in enumerate(args[2:]):
                    if count % 2 != 0:
                        continue
                    try:
                        variantdict[text]=args[count+3]
                    except IndexError:
                        break
                type_ = convert_to_type(args[1])
                id_ = member_asset(client.party.me, convert_to_asset(args[1]))
                variants = client.party.me.create_variants(item='AthenaCharacter',**variantdict)
                print(variants)
                if await change_asset(client, message.author.id, type_, id_, variants, client.party.me.enlightenments) is False:
                    await reply(message, l('locked'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_changing_asset'))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['setvariant']}] [ID] [variant] [{l('number')}]")
            except Exception:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0] in commands['addvariant'].split(','):
            try:
                if True not in [args[1] in commands[key].split(',') for key in ("outfit", "backpack", "pet", "pickaxe")]:
                    await reply(message, f"[{commands['addvariant']}] [[{commands['outfit']}] / [{commands['backpack']}] / [{commands['pet']}] / [{commands['pickaxe']}]]")
                    return
                variantdict={}
                for count,text in enumerate(args[2:]):
                    if count % 2 != 0:
                        continue
                    try:
                        variantdict[text]=args[count+3]
                    except IndexError:
                        break
                type_ = convert_to_type(args[1])
                id_ = member_asset(client.party.me, convert_to_asset(args[1]))
                variants = client.party.me.create_variants(item='AthenaCharacter',**variantdict)
                variants += eval(f"client.party.me.{convert_to_asset(args[1])}_variants")
                if await change_asset(client, message.author.id, type_, id_, variants, client.party.me.enlightenments) is False:
                    await reply(message, l('locked'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_changing_asset'))
            except IndexError:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, f"[{commands['addvariant']}] [ID] [variant] [{l('number')}]")
            except Exception:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif True in [args[0] in commands[key].split(',') for key in ("outfitasset", "backpackasset", "pickaxeasset", "emoteasset")]:
            type_ = convert_to_type(args[0])
            try:
                if rawcontent == '':
                    await reply(message, f"[{commands[f'{type_}asset']}] [{l('assetpath')}]")
                    return
                if await change_asset(client, message.author.id, type_, rawcontent) is False:
                    await reply(message, l('locked'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_changing_asset'))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif True in [args[0].lower().startswith(id_) for id_ in ("cid_", "bid_", "petcarrier_", "pickaxe_id_", "eid_", "emoji_", "toy_")]:
            try:
                type_ = convert_to_type("_".join(args[0].split('_')[:-1]) + "_")
                if await change_asset(client, message.author.id, type_, args[0]) is False:
                    await reply(message, l('locked'))
            except fortnitepy.HTTPException:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error_while_changing_asset'))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        elif args[0].lower().startswith('playlist_'):
            try:
                await client.party.set_playlist(args[0])
                await reply(message, l('set_playlist', args[0]))
                data['fortnite']['playlist']=args[0]
            except fortnitepy.Forbidden:
                if data['loglevel'] == 'debug':
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('not_party_leader'))
            except Exception:
                print(red(traceback.format_exc()))
                dstore(name,f'>>> {traceback.format_exc()}')
                await reply(message, l('error'))

        else:
            if ': ' in message.content:
                return
            if args[0].isdigit() and client.select.get(message.author.id) is not None:
                try:
                    if int(args[0]) == 0:
                        await reply(message, l('please_enter_valid_number'))
                        return
                    exec_ = client.select[message.author.id]["exec"][int(args[0])-1]
                    variable=globals()
                    variable.update(locals())
                    if client.select[message.author.id].get("variable") is not None:
                        variable.update(client.select[message.author.id]["variable"][int(args[0])-1])
                    await aexec(exec_, variable)
                except IndexError:
                    if data['loglevel'] == 'debug':
                        print(red(traceback.format_exc()))
                        dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l('please_enter_valid_number'))
                except Exception:
                    print(red(traceback.format_exc()))
                    dstore(name,f'>>> {traceback.format_exc()}')
                    await reply(message, l('error'))
            else:
                result = await loop.run_in_executor(None, search_item, data["lang"], "name", content, "item")
                if result is None:
                    result = await loop.run_in_executor(None, search_item, "en", "name", content, "item")
                if result is not None:
                    if len(result) > 30:
                        await reply(message, l('too_many_items', str(len(result))))
                        return
                    if len(result) == 1:
                        if await change_asset(client, message.author.id, result[0]["type"]["value"], result[0]['id']) is True:
                            await reply(message, f"{result[0]['type']['displayValue']}: {result[0]['name']} | {result[0]['id']}")
                        else:
                            await reply(message, l('locked'))
                    else:
                        text = str()
                        for count, item in enumerate(result):
                            text += f"\n{count+1} {item['type']['displayValue']}: {item['name']} | {item['id']}"
                        text += f"\n{l('enter_to_change_asset')}"
                        await reply(message, text)
                        client.select[message.author.id] = {"exec": [f"await change_asset(client, '{message.author.id}', '{item['type']['value']}', '{item['id']}')" for item in result]}

#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================
#========================================================================================================================

clients = []
for count, credential in enumerate(credentials.items()):
    email = credential[0]
    password = credential[1]
    try:
        device_auth_details = get_device_auth_details().get(email, {})
        client = fortnitepy.Client(
            platform=fortnitepy.Platform(data['fortnite']['platform'].upper()),
            status=data['fortnite']['status'],
            auth=fortnitepy.AdvancedAuth(
                email=email,
                password=password,
                prompt_exchange_code=True,
                prompt_exchange_code_if_throttled=True,
                delete_existing_device_auths=False,
                **device_auth_details
            ),
            default_party_member_config=fortnitepy.DefaultPartyMemberConfig(
                meta=[
                    partial(ClientPartyMember.set_outfit, data['fortnite']['cid'].replace('cid','CID',1)),
                    partial(ClientPartyMember.set_backpack, data['fortnite']['bid'].replace('bid','BID',1)),
                    partial(ClientPartyMember.set_pickaxe, data['fortnite']['pickaxe_id'].replace('pickaxe_id','Pickaxe_ID',1)),
                    partial(ClientPartyMember.set_battlepass_info, has_purchased=True, level=data['fortnite']['tier'], self_boost_xp=data['fortnite']['xpboost'], friend_boost_xp=data['fortnite']['friendxpboost']),
                    partial(ClientPartyMember.set_banner, icon=data['fortnite']['banner'], color=data['fortnite']['banner_color'], season_level=data['fortnite']['level']),
                ]
            )
        )
    except ValueError:
        print(red(traceback.format_exc()))
        print(red(l('error_while_setting_client')))
        dstore(client.user.display_name,f'>>> {traceback.format_exc()}')
        dstore(client.user.display_name,l('error_while_setting_client'))
        continue
    
    client.eid=data['fortnite']['eid']
    client.isready=False
    client.acceptinvite_interval=True
    client.stopcheck=False
    client.outfitlock=False
    client.backpacklock=False
    client.pickaxelock=False
    client.emotelock=False
    client.owner=None
    client.prevoutfit=None
    client.prevoutfitvariants=None
    client.prevbackpack=None
    client.prevbackpackvariants=None
    client.prevpickaxe=None
    client.prevpickaxevariants=None
    client.prevmessage={}
    client.select={}
    client.invitelist=[]
    client.whisper=data['fortnite']['whisper']
    client.partychat=data['fortnite']['partychat']
    client.discord=data['discord']['discord']
    client.whisperperfect=data['fortnite']['disablewhisperperfectly']
    client.partychatperfect=data['fortnite']['disablepartychatperfectly']
    client.discordperfect=data['discord']['disablediscordperfectly']
    client.joinmessageenable=data['fortnite']['joinmessageenable']
    client.randommessageenable=data['fortnite']['randommessageenable']
    client.outfitmimic=data['fortnite']['outfitmimic']
    client.backpackmimic=data['fortnite']['backpackmimic']
    client.pickaxemimic=data['fortnite']['pickaxemimic']
    client.emotemimic=data['fortnite']['emotemimic']
    client.acceptinvite=data['fortnite']['acceptinvite']
    client.acceptfriend=data['fortnite']['acceptfriend']

    client.add_event_handler('device_auth_generate', event_device_auth_generate)
    client.add_event_handler('restart', event_restart)
    client.add_event_handler('party_invite', event_party_invite)
    client.add_event_handler('friend_request', event_friend_request)
    client.add_event_handler('friend_add', event_friend_add)
    client.add_event_handler('friend_remove', event_friend_remove)
    client.add_event_handler('party_member_join', event_party_member_join)
    client.add_event_handler('party_member_leave', event_party_member_leave)
    client.add_event_handler('party_member_confirm', event_party_member_confirm)
    client.add_event_handler('party_member_kick', event_party_member_kick)
    client.add_event_handler('party_member_promote', event_party_member_promote)
    client.add_event_handler('party_member_update', event_party_member_update)
    client.add_event_handler('party_member_disconnect', event_party_member_disconnect)
    client.add_event_handler('party_member_chatban', event_party_member_chatban)
    client.add_event_handler('party_update', event_party_update)
    client.add_event_handler('friend_message', event_friend_message)
    client.add_event_handler('party_message', event_party_message)

    clients.append(client)

try:
    fortnitepy.run_multiple(
        clients,
        ready_callback=event_ready,
        all_ready_callback=lambda: print(green(f"[{now_()}] {l('all_login')}")) if len(clients) > 1 else print('')
    )
except fortnitepy.AuthException as e:
    if "errors.com.epicgames.account.oauth.exchange_code_not_found" in e.args[0]:
        print(red(traceback.format_exc()))
        print(f'[{now_()}] {l("exchange_code_error")}')
        dstore(l("bot"),f'>>> {traceback.format_exc()}')
        dstore(l("bot"),f'>>> {l("exchange_code_error")}')
    else:
        print(red(traceback.format_exc()))
        print(red(f'[{now_()}] {l("login_failed")}'))
        dstore(l("bot"),f'>>> {traceback.format_exc()}')
        dstore(l("bot"),f'>>> {l("login_failed")}')
    kill=True
    sys.exit(1)
except KeyboardInterrupt:
    kill=True
    sys.exit(1)
except Exception:
    print(red(traceback.format_exc()))
    print(red(f'[{now_()}] {l("failed_to_load_account")}'))
    dstore(l("bot"),f'>>> {traceback.format_exc()}')
    dstore(l("bot"),f'>>> {l("failed_to_load_account")}')
    kill=True
    sys.exit(1)
