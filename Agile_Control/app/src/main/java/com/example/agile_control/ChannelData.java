package com.example.agile_control;

import org.json.JSONException;
import org.json.JSONObject;

public class ChannelData {
	String node_id;
	String name;
	String state;
	String id;
	String IO;
	int var_value;


	ChannelData(JSONObject channel)
	{
		try {
			this.name = channel.getString("name");
			this.state = channel.getString("state");
			this.node_id = channel.getString("state");
			this.id = channel.getString("id");
			this.IO = channel.getString("IO");
			this.var_value = channel.getInt("var_value");
		} catch (JSONException e) {
			e.printStackTrace();
		}
	}
}
